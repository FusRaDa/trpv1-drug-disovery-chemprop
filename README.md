# TRPV1 drug discovery using machine learning - Chemprop & ChemTSV2

### Process steps
00. parse data from ChEMBL of molecule interactions with TRPV1
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/00_trpv1_agonists_data.ipynb

01. train and test ChemProp model
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/01_trpv1_chemprop_train_test.ipynb

02. make predictions with model
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/02_trpv1_chemprop_predict.ipynb

03. understand the additional properties of a compound in the ChEMBL database and determine what analytical steps to take.
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/03_trpv1_agonist_data_multiprop.ipynb

04. find trends in the training/testing data for TRPV1 using random forest (MDI & Permutations).
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/04_trpv1_agonist_data_trends.ipynb

05. train a new chemprop model with the multiple properties shown be significant from step 4
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/05_trpv1_chemprop_train_test.ipynb

06. make predictions on new multi-property chemprop model (refer to step 3).
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/06_trpv1_chemprop_predict.ipynb

07. begin working on ChemTSV2 as a compound generative model - testing with default settings with very simple/crude grading criteria
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/07_chemtsv2_compound_generator.ipynb

08. gather training/testing data from ChEMBL for making chemprop opioid-receptor models: MOR, DOR, KOR, and Nociceptin
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/08_chemtsv2_analysis_and_data.ipynb

09. train/test 4 new chemprop models for opioid receptors as a single-property model: MOR, DOR, KOR, and Nociceptin
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/09_chemtsv2_train_and_test.ipynb

10. generate compounds with ChemTSV2 but with the 4 new opioid-receptor chemprop models as a negative criteria.
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/10_chemtsv2_compound_generator.ipynb

11. gather training/testing data with multiple properties - refer to step 8
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/11_opioid_agonist_data_multiprop.ipynb

12. recreate the 4 opioid models but build them with multiple properties - refer to step 9
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/12_chemtsv2_train_and_test_multiprop.ipynb

13. generate compounds again but use the multi-property models (TRPV1, MOR, DOR, KOR, and Nociceptin)
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/13_chemtsv2_compound_generator.ipynb

14. compare the generative outputs from both runs that were using the single-prop models and multi-prop models.
  * View notebook: https://github.com/FusRaDa/trpv1-drug-disovery-chemprop/blob/main/14_chemtsv2_output_analysis.ipynb


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

- Ways to improve the grading criteria for ChemTSV2 compound generator?


### Tools to look into:
- Chemprop: https://chemprop.readthedocs.io/en/latest/index.html - IMPLEMENTED
- ChemTSV2: https://github.com/molecule-generator-collection/ChemTSv2?tab=readme-ov-file - IMPLEMENTED
- Torch Molecule: https://github.com/liugangcode/torch-molecule


### Citations
Esther Heid, Kevin P. Greenman, Yunsie Chung, Shih-Cheng Li, David E. Graff, Florence H. Vermeire, Haoyang Wu, William H. Green, and Charles J. McGill. Chemprop: a machine learning package for chemical property prediction. Journal of Chemical Information and Modeling, 64(1):9–17, 2024. PMID: 38147829. URL: https://doi.org/10.1021/acs.jcim.3c01250, arXiv:https://doi.org/10.1021/acs.jcim.3c01250, doi:10.1021/acs.jcim.3c01250.

Ishida, S. and Aasawat, T. and Sumita, M. and Katouda, M. and Yoshizawa, T. and Yoshizoe, K. and Tsuda, K. and Terayama, K. (2023). ChemTSv2: Functional molecular design using de novo molecule generator. WIREs Computational Molecular Science https://wires.onlinelibrary.wiley.com/doi/10.1002/wcms.1680

Kevin Yang, Kyle Swanson, Wengong Jin, Connor Coley, Philipp Eiden, Hua Gao, Angel Guzman-Perez, Timothy Hopper, Brian Kelley, Miriam Mathea, Andrew Palmer, Volker Settels, Tommi Jaakkola, Klavs Jensen, and Regina Barzilay. Analyzing learned molecular representations for property prediction. Journal of Chemical Information and Modeling, 59(8):3370–3388, 2019. PMID: 31361484. URL: https://doi.org/10.1021/acs.jcim.9b00237, arXiv:https://doi.org/10.1021/acs.jcim.9b00237, doi:10.1021/acs.jcim.9b00237.

Santos R., A comprehensive map of molecular drug targets Nat. Rev. Drug Disc. 16(1):19-34

Yang, X., Zhang, J., Yoshizoe, K., Terayama, K., & Tsuda, K. (2017). ChemTS: an efficient python library for de novo molecular generation. Science and Technology of Advanced Materials, 18(1), 972–976. https://doi.org/10.1080/14686996.2017.1401424

Yang, X., Aasawat, T., & Yoshizoe, K. (2021). Practical Massively Parallel Monte-Carlo Tree Search Applied to Molecular Design. In International Conference on Learning Representations. https://openreview.net/forum?id=6k7VdojAIK