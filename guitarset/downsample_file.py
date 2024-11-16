import os
import librosa
import soundfile as sf

from utils import print_wav_info

infile = 'test.wav'
outfile = 'test_8kHz.wav'
samplerate = 8000

y, sr = librosa.load(infile, sr=samplerate)
sf.write(outfile, y, sr)
print_wav_info(outfile)

print('Done!')
