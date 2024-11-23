import os
import librosa
import soundfile as sf

from utils import print_wav_info

audiodir = 'synth_mono_3s/synth_mono'
samplerate = 16000

for dirpath, dirnames, filenames in os.walk(audiodir):
    if dirpath != audiodir:
        for f in filenames:
            fpath = os.path.join(dirpath, f)
            y, sr = librosa.load(fpath, sr=samplerate)
            sf.write(fpath, y, sr)

print('Done!')
