import torch
from asteroid.models import BaseModel
from asteroid.models import DPRNNTasNet 
import soundfile as sf

model = DPRNNTasNet(n_src=2, sample_rate=16000)

model.load_state_dict(torch.load('model_16k', weights_only=True))
model.eval()

model.separate("demo3_mix_16k.wav", force_overwrite=True, resample=True)
