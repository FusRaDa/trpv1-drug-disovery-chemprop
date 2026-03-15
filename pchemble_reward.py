import sys
import numpy as np
from rdkit.Chem import Descriptors
from chemtsv2.abc import Reward
from chemprop.models.model import MPNN
from chemprop import data, featurizers, models
from lightning import pytorch as pl
from rdkit import Chem
import torch


TRPV1 = '/content/drive/MyDrive/Colab_Notebooks/TRPV1-drug-discovery-research/models/best-epoch=52-val_loss=0.33.ckpt'
MOR = '/content/drive/MyDrive/Colab_Notebooks/TRPV1-drug-discovery-research/models/MOR_best-epoch=43-val_loss=0.35.ckpt'
DOR = '/content/drive/MyDrive/Colab_Notebooks/TRPV1-drug-discovery-research/models/DOR_best-epoch=48-val_loss=0.33.ckpt'
KOR = '/content/drive/MyDrive/Colab_Notebooks/TRPV1-drug-discovery-research/models/KOR_best-epoch=56-val_loss=0.41.ckpt'
NOCICEPTIN = '/content/drive/MyDrive/Colab_Notebooks/TRPV1-drug-discovery-research/models/Nociceptin_best-epoch=58-val_loss=0.43.ckpt'


def predict_receptivity(mol, model_path):
  # turn mol to smiles
  smiles = []
  smile = Chem.MolToSmiles(mol)
  smiles.append(smile)

  # load model
  checkpoint_path = model_path # CHANGE THIS TO WHERE THE MODEL .CKPT FILE IS SAVED
  mpnn = MPNN.load_from_checkpoint(checkpoint_path)

  # assign data
  test_data = [data.MoleculeDatapoint.from_smi(smi) for smi in smiles]

  # set model vars
  featurizer = featurizers.SimpleMoleculeMolGraphFeaturizer()
  test_dset = data.MoleculeDataset(test_data, featurizer=featurizer)
  test_loader = data.build_dataloader(test_dset, shuffle=False)

  # predict
  with torch.inference_mode():
    trainer = pl.Trainer(
        logger=None,
        enable_progress_bar=True,
        accelerator="cuda",
        devices=1
    )
    test_preds = trainer.predict(mpnn, test_loader)

  # extract only pchembl value
  return test_preds[0][0].numpy()[0]


class pchemble_reward(Reward):
  def get_objective_functions(conf):
    # we need to hook our chemprop model here to predict a pChEMBLE value
    def predict_trpv1_receptivity(mol):
      return predict_receptivity(mol, TRPV1)

    def predict_mor_receptivity(mol):
      return predict_receptivity(mol, MOR)

    def predict_dor_receptivity(mol):
      return predict_receptivity(mol, DOR)

    def predict_kor_receptivity(mol):
      return predict_receptivity(mol, KOR)

    def predict_nociceptin_receptivity(mol):
      return predict_receptivity(mol, NOCICEPTIN)

    return [predict_trpv1_receptivity, predict_mor_receptivity, predict_dor_receptivity, predict_kor_receptivity, predict_nociceptin_receptivity]

  def calc_reward_from_objective_values(values, conf):
    max_pchemble_val = 10 # lets arbitrarily set max score to 10

    # all values
    trpv1_pchembl_pred = values[0]
    mor_pchembl_pred = values[1]
    dor_pchembl_pred = values[2]
    kor_pchembl_pred = values[3]
    nociceptin_pchembl_pred = values[4]

    # positive criteria - get all favorable traits
    trpv1_score = trpv1_pchembl_pred / max_pchemble_val

    # negative criteria - get all unfavorable traits
    negative_scores = []
    mor_score = mor_pchembl_pred / max_pchemble_val
    dor_score = dor_pchembl_pred / max_pchemble_val
    kor_score = kor_pchembl_pred / max_pchemble_val
    nociceptin_score = nociceptin_pchembl_pred / max_pchemble_val

    # store positive scores in array
    positive_scores = []
    positive_scores.append(trpv1_score)

    # store negative scores in array
    negative_scores = []
    negative_scores.append(mor_score)
    negative_scores.append(dor_score)
    negative_scores.append(kor_score)
    negative_scores.append(nociceptin_score)

    positive_sum = sum(positive_scores) / len(positive_scores)
    negative_sum = sum(negative_scores) / len(negative_scores)

    sum_of_scores = positive_sum - negative_sum
    return sum_of_scores
