# Asteroid is based on PyTorch and PyTorch-Lightning.
from torch import optim
from pytorch_lightning import Trainer
from torch.utils.data import DataLoader

# We train the same model architecture that we used for inference above.
from asteroid.models import DPRNNTasNet

# In this example we use Permutation Invariant Training (PIT) and the SI-SDR loss.
from asteroid.losses import pairwise_neg_sisdr, PITLossWrapper

# MiniLibriMix is a tiny version of LibriMix (https://github.com/JorisCos/LibriMix),
# which is a free speech separation dataset.
from asteroid.data import LibriMix

# Asteroid's System is a convenience wrapper for PyTorch-Lightning.
from asteroid.engine import System

# import my custom dataset class
from guitarset_dataset import GuitarSetDataset

# hyperparameter variables
BATCH_SIZE = 16
MAX_EPOCHS = 1

# create the train and validation paths
train_path = "./dataset_s1s6/metadata/train.csv"
val_path = "./dataset_s1s6/metadata/val.csv"

# instantiate GuitarSetDataset object(s)
train_set = GuitarSetDataset(train_path)
val_set = GuitarSetDataset(val_path)

# get dataloader
train_loader = DataLoader(train_set, batch_size=BATCH_SIZE)
val_loader = DataLoader(val_set, batch_size=BATCH_SIZE)

train_features, train_labels = next(iter(train_loader))
val_features, val_labels = next(iter(val_loader))
print(f"Train feature batch shape: {train_features.size()}")
print(f"Train labels batch shape: {train_labels.size()}")
print(f"Val feature batch shape: {val_features.size()}")
print(f"Val labels batch shape: {val_labels.size()}")

# Tell DPRNN that we want to separate to 2 sources.
model = DPRNNTasNet(n_src=2, sample_rate=44100)

# PITLossWrapper works with any loss function.
loss = PITLossWrapper(pairwise_neg_sisdr, pit_from="pw_mtx")

optimizer = optim.Adam(model.parameters(), lr=1e-3)

system = System(model, optimizer, loss, train_loader, val_loader)

# Train for 1 epoch using a single GPU. If you're running this on Google Colab,
# be sure to select a GPU runtime (Runtime → Change runtime type → Hardware accelarator).
trainer = Trainer(max_epochs=MAX_EPOCHS)
trainer.fit(system)

model.separate("test2.wav", force_overwrite=True)
