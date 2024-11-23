import torch
from asteroid.models import BaseModel
from asteroid.models import DPRNNTasNet 
import soundfile as sf

model = DPRNNTasNet(n_src=2, sample_rate=8000)

model.load_state_dict(torch.load('my_model', weights_only=True))
model.eval()

model.separate("test2.wav", force_overwrite=True, resample=True)
