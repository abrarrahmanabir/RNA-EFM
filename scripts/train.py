from lightning import Trainer
from lightning.pytorch.callbacks import ModelCheckpoint
import sys

sys.path.append("rnaefm")
from data.dataloader import RFDataModule
from models.rnaefm import rnaefm
from models.inverse_folding import InverseFoldingModel

RF_DATA_FOLDER = "rnaefm/data/rf_data"
DATASET_PKL = "rnaefm/data/rf2na_dataset.pickle"

if __name__ == "__main__":
    print("Training rnaefm Model.")

    data_module = RFDataModule(rf_data_folder=RF_DATA_FOLDER, dataset_pkl=DATASET_PKL, batch_size=1)
    train_dataloader = data_module.train_dataloader()
    val_dataloader = data_module.val_dataloader()

    rnaefm = rnaefm()
    rnaefm.denoise_model = InverseFoldingModel()

    # checkpoint_callback = ModelCheckpoint(dirpath="newmodel", save_top_k=3, monitor="val_loss", filename="new_rnaefm-{epoch:02d}-{val_loss:.2f}")
    # trainer = Trainer(devices=1, enable_checkpointing=True, callbacks=[checkpoint_callback], check_val_every_n_epoch=3, max_epochs=500) 
    # trainer.fit(rnaefm, train_dataloader, val_dataloader)

    checkpoint_callback = ModelCheckpoint(
        dirpath="newmodel", 
        filename="rnaefm-{epoch:02d}"
    )

    # Trainer: Disable validation
    trainer = Trainer(
        devices=1, 
        enable_checkpointing=True, 
        callbacks=[checkpoint_callback], 
        max_epochs=100
    )

    # Train without validation
    trainer.fit(rnaefm, train_dataloader)


