# TRPV1 drug discovery using machine learning - chemprop

### Process steps
1. parse data from ChEMBL of molecule interactions with TRPV1
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/0_trpv1_agonists_data.ipynb

2. train and test ChemProp model
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/1_trpv1_chemprop_train_test.ipynb

3. make predictions with model
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/2_trpv1_chemprop_predict.ipynb


### Pros and cons
* The power behind machine learning is **Pattern Recognition**. Chemprop is based off linear regression where it produces a trending line between the chemical structure (SMILES) and the target (in this case, pChEMBL values). Knowing this, machine learning cannot replace an experienced chemist who understands the actual implications but rather serves as guide to what is feasible or not.

* To clariify, pChEMBL values is a global/standard value used to compare compound potency of each row of data in the database.
  * Here is an example of compounds that have been recorded to having interaction with TRPV1: https://www.ebi.ac.uk/chembl/explore/activities/STATE_ID:EaSiRjZbYZGLqZd7CgNV7g%3D%3D
  * Notice the standard type (method of analysis) differs. The pChEMBL aims to standardized each row of data so that we can compare the potency or effectivity of the compounds listed.


### Next steps and improvements
* Train a Chemprop model to also consider multiple targets including the pChEMBL value. 
  * Targets to predict could be: MW, solubility, affinity, etc... (Of course we will have to gather this data from databases)

* Consider creating a compound generator as in instead of inputting SMILES to predict values, we can input values to predict SMILES.

* Further validation of training/testing model data and increasing sample size for a more accurate prediction.

* Further understand all mechanisms involved in how RTX works and how its naturally synthesized by Euphorbia resinifera.

* Learn from the best! There are other approaches to solving this problem that doesn't involve being in front of a computer.


### Questions to ask to get the gears rolling...
- What chemical properties contribute to a more effective non-opoid painkiller?

- Is RTX the most effective non-opoid pain killer that we know of?
  - Quick Google search: Suzetrigine?



