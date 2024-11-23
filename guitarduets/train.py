import torch

# Asteroid is based on PyTorch and PyTorch-Lightning.
from torch import optim
from pytorch_lightning import Trainer
from torch.utils.data import DataLoader

# We train the same model architecture that we used for inference above.
from asteroid.models import DPRNNTasNet

# In this example we use Permutation Invariant Training (PIT) and the SI-SDR loss.
from asteroid.losses import pairwise_neg_sisdr, PITLossWrapper

# Asteroid's System is a convenience wrapper for PyTorch-Lightning.
from asteroid.engine import System

# import my custom dataset class
from guitarduet_dataset import GuitarDuetDataset

# hyperparameter variables
BATCH_SIZE = 16
MAX_EPOCHS = 10

# create the train and validation paths
train_path = "data_synth-real_3s_16k/metadata/train.csv"
val_path = "data_synth-real_3s_16k/metadata/val.csv"

# instantiate GuitarDuetDataset object(s)
train_set = GuitarDuetDataset(train_path, sample_rate=16000)
val_set = GuitarDuetDataset(val_path, sample_rate=16000)

# get dataloader
train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, num_workers=10)
val_loader = DataLoader(val_set, batch_size=BATCH_SIZE, num_workers=2)

train_features, train_labels = next(iter(train_loader))
val_features, val_labels = next(iter(val_loader))
print(f"Train feature batch shape: {train_features.size()}")
print(f"Train labels batch shape: {train_labels.size()}")
print(f"Val feature batch shape: {val_features.size()}")
print(f"Val labels batch shape: {val_labels.size()}")

# Tell DPRNN that we want to separate to 2 sources.
model = DPRNNTasNet(n_src=2, sample_rate=16000)

# PITLossWrapper works with any loss function.
loss = PITLossWrapper(pairwise_neg_sisdr, pit_from="pw_mtx")

optimizer = optim.Adam(model.parameters(), lr=1e-3)

system = System(model, optimizer, loss, train_loader, val_loader)

# train and save model
trainer = Trainer(max_epochs=MAX_EPOCHS)
trainer.fit(system)
torch.save(model.state_dict(), 'model_16k')

# separate a demo track
model.separate("demo3_mix_16k.wav", force_overwrite=True, resample=False)
