"""Ligand-conditioned molecular generation with EnsCondFlow.

Vendored from https://github.com/rssrwn/ensemble-cond-design at commit 5d557af (MIT).
Four local patches were applied to the vendored copy:
  - repr/vocab.py: PEP 695 generic syntax rewritten as Generic[T] so the code runs on
    Python 3.11 rather than requiring 3.12+.
  - scriptutil.py, models/fm.py: the enscondflow.eval.docking import is guarded, since
    vina and meeko are conda-only and never reached on the ligand-conditioned path.
  - util/geometry/optimise.py: the xtb import is guarded for the same reason.

The checkpoint (enscond.ckpt, CC-BY-4.0, Zenodo record 22485204) is not tracked in git;
it is synced through eosvc into model/checkpoints/.

Sampling parameters deviate from the upstream defaults. At the upstream settings
(cfg_gamma=1.0, shape_std_dev=0.3) the model reproduces the reference compound in 8 of
10 samples. cfg_gamma is the dominant lever on diversity, so it is lowered to 0.5 and
shape_std_dev raised to 0.8; the generator is then over-sampled and the reference
compound and duplicates are removed from the returned set.
"""

import os

import lightning as L
from rdkit import Chem
from rdkit.Chem import AllChem

from enscondflow.repr import GraphMol
from enscondflow.sample import load_pretrained, sample_molecules

N_OUTPUTS = 10
OVERSAMPLE = 2
SEED = 12345
CFG_GAMMA = 0.5
SHAPE_STD_DEV = 0.8

CHECKPOINT = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "checkpoints", "enscond.ckpt"
)

_model = None


def _get_model():
    """Load the checkpoint once and reuse it across input compounds."""
    global _model
    if _model is None:
        _model = load_pretrained(CHECKPOINT, device="cpu")
    return _model


def _reference(smiles):
    """Build the 3D reference the model conditions on, or None if the SMILES is unusable."""
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    mol = Chem.AddHs(mol)
    if AllChem.EmbedMolecule(mol, randomSeed=SEED) != 0:
        return None
    AllChem.MMFFOptimizeMolecule(mol)
    return GraphMol.from_rdkit(mol)


def generate(smiles, n_outputs=N_OUTPUTS):
    """Return n_outputs generated SMILES for one input compound, padded with empty strings."""
    reference = _reference(smiles)
    if reference is None:
        return [""] * n_outputs

    # verbose=False keeps Lightning's "Seed set to ..." banner off stderr, which
    # Ersilia's runner otherwise reports as an execution error.
    L.seed_everything(SEED, workers=True, verbose=False)
    n_sampled = n_outputs * OVERSAMPLE
    mols = sample_molecules(
        _get_model(),
        n_mols=n_sampled,
        batch_size=n_sampled,
        reference=reference,
        profile_cond="profile",
        cfg_gamma=CFG_GAMMA,
        shape_std_dev=SHAPE_STD_DEV,
    )

    try:
        input_canonical = Chem.CanonSmiles(smiles)
    except Exception:
        input_canonical = None

    generated, seen = [], set()
    for mol in mols:
        if mol is None:
            continue
        try:
            smi = Chem.MolToSmiles(mol)
        except Exception:
            continue
        if not smi or smi in seen or smi == input_canonical:
            continue
        seen.add(smi)
        generated.append(smi)
        if len(generated) == n_outputs:
            break

    return generated + [""] * (n_outputs - len(generated))
