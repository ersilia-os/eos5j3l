# imports
import sys

from ersilia_pack_utils.core import read_smiles, write_out

from predict import N_OUTPUTS, generate


def my_model(smiles_list):
    return [generate(smi) for smi in smiles_list]


if __name__ == "__main__":
    # parse arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # read SMILES from .csv file, assuming one column with header
    _, smiles_list = read_smiles(input_file)

    # run model
    outputs = my_model(smiles_list)

    # check input and output have the same length
    assert len(smiles_list) == len(outputs)

    header = [f"smi_{str(i).zfill(1)}" for i in range(N_OUTPUTS)]

    # write output in a .csv file
    write_out(outputs, header, output_file)
