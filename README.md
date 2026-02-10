# TRPV1 drug discovery using machine learning - chemprop

### Process steps
1. parse data from ChEMBL of molecule interactions with TRPV1
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/0_trpv1_agonists_data.ipynb

2. train and test ChemProp model
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/1_trpv1_chemprop_train_test.ipynb

3. make predictions with model
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/2_trpv1_chemprop_predict.ipynb


### Pros and cons
* The power behind machine learning is **Pattern Recognition**. Chemprop is based off linear regression where it produces a trending line between the chemical structure (SMILES) and the target (in this case, pChEMBL values). Knowing this, machine learning cannot replace an experienced chemist who understands the actual implications but rather serves as a guide to what is feasible or not.

* To clarify, pChEMBL values is a global/standard value used to compare compound potency of each row of data in the database.
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

- Is RTX the most effective non-opioid pain killer that we know of?
  - Quick Google search: Suzetrigine?


### Citations

Kevin Yang, Kyle Swanson, Wengong Jin, Connor Coley, Philipp Eiden, Hua Gao, Angel Guzman-Perez, Timothy Hopper, Brian Kelley, Miriam Mathea, Andrew Palmer, Volker Settels, Tommi Jaakkola, Klavs Jensen, and Regina Barzilay. Analyzing learned molecular representations for property prediction. Journal of Chemical Information and Modeling, 59(8):3370–3388, 2019. PMID: 31361484. URL: https://doi.org/10.1021/acs.jcim.9b00237, arXiv:https://doi.org/10.1021/acs.jcim.9b00237, doi:10.1021/acs.jcim.9b00237.

Esther Heid, Kevin P. Greenman, Yunsie Chung, Shih-Cheng Li, David E. Graff, Florence H. Vermeire, Haoyang Wu, William H. Green, and Charles J. McGill. Chemprop: a machine learning package for chemical property prediction. Journal of Chemical Information and Modeling, 64(1):9–17, 2024. PMID: 38147829. URL: https://doi.org/10.1021/acs.jcim.3c01250, arXiv:https://doi.org/10.1021/acs.jcim.3c01250, doi:10.1021/acs.jcim.3c01250.

Santos R., A comprehensive map of molecular drug targets Nat. Rev. Drug Disc. 16(1):19-34