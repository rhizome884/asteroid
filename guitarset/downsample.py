import os
import librosa
import soundfile as sf

from utils import print_wav_info

audiodir = 'dataset_s1s6_8kHz'
samplerate = 8000

for dirpath, dirnames, filenames in os.walk(audiodir):
    if dirpath != audiodir:
        for f in filenames:
            fpath = os.path.join(dirpath, f)
            print_wav_info(fpath)
            y, sr = librosa.load(fpath, sr=samplerate)
            sf.write(fpath, y, sr)
            print_wav_info(fpath)

print('Done!')
