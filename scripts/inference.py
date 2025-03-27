from lightning import Trainer
from lightning.pytorch.callbacks import ModelCheckpoint
import sys

sys.path.append("rnaefm")
from data.dataloader import RFDataModule
from models.rnaefm import rnaefm
from models.inverse_folding import InverseFoldingModel

RF_DATA_FOLDER = "rnaefm/data/rf_data"
DATASET_PKL = "rnaefm/data/rf2na_dataset.pickle" #     rnaefm/data/seq_sim_dataset.pickle

if __name__ == "__main__":
    print("Running rnaefm Inference.")

    data_module = RFDataModule(rf_data_folder=RF_DATA_FOLDER, dataset_pkl=DATASET_PKL, batch_size=1)
    test_dataloader = data_module.test_dataloader()

    rnaefm = rnaefm.load_from_checkpoint("newmodel/rnaefm-epoch=06.ckpt")  # newmodel/rnaefm-epoch=06.ckpt  checkpoints/seq-sim-rnaefm-epoch32.ckpt

    trainer = Trainer(devices=1)
    trainer.predict(rnaefm, dataloaders=test_dataloader)