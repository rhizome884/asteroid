import os
import librosa
import soundfile as sf

from utils import print_wav_info

file = 'downsample/demo3_mix.wav'
sample_rate = 16000

y, sr = librosa.load(file, sr=sample_rate)
sf.write('demo3_mix_16k.wav', y, sr)

