# Ensemble-Conditioned Molecular Design

Generates 10 molecules conditioned on the 3D shape and pharmacophore profile of an input compound, using flow matching with ensemble-conditioned guidance from AstraZeneca and Chalmers. Trained on 300K GEOM-Drugs molecules with CREST conformer ensembles and 35K PDB-derived protein-ligand complexes. Drug-like inputs yield structurally distinct compounds; small rigid molecules are instead often reproduced, so guidance is weakened from the published defaults and the input compound and duplicates are filtered from the returned set.



## Information
### Identifiers
- **Ersilia Identifier:** `eos5j3l`
- **Slug:** `enscondflow-shape`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Generation`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Compound generation`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `10`
- **Output Consistency:** `Fixed`
- **Interpretation:** 10 generated molecules sharing the 3D shape and pharmacophore profile of the input compound.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| smi_0 | string |  | Generated molecule index 0 matching the 3D shape and pharmacophore profile of the input compound |
| smi_1 | string |  | Generated molecule index 1 matching the 3D shape and pharmacophore profile of the input compound |
| smi_2 | string |  | Generated molecule index 2 matching the 3D shape and pharmacophore profile of the input compound |
| smi_3 | string |  | Generated molecule index 3 matching the 3D shape and pharmacophore profile of the input compound |
| smi_4 | string |  | Generated molecule index 4 matching the 3D shape and pharmacophore profile of the input compound |
| smi_5 | string |  | Generated molecule index 5 matching the 3D shape and pharmacophore profile of the input compound |
| smi_6 | string |  | Generated molecule index 6 matching the 3D shape and pharmacophore profile of the input compound |
| smi_7 | string |  | Generated molecule index 7 matching the 3D shape and pharmacophore profile of the input compound |
| smi_8 | string |  | Generated molecule index 8 matching the 3D shape and pharmacophore profile of the input compound |
| smi_9 | string |  | Generated molecule index 9 matching the 3D shape and pharmacophore profile of the input compound |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`

### Resource Consumption


### References
- **Source Code**: [https://github.com/rssrwn/ensemble-cond-design](https://github.com/rssrwn/ensemble-cond-design)
- **Publication**: [https://doi.org/10.48550/arXiv.2609.15077](https://doi.org/10.48550/arXiv.2609.15077)
- **Publication Type:** `Preprint`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos5j3l
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos5j3l
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
