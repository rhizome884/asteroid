from pydub import AudioSegment
import os

INPUT_PATH = "synth"
OUTPUT_PATH = "synth_mono"

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

for dirpath, dirnames, filenames in os.walk(INPUT_PATH):
    
    if dirpath != INPUT_PATH:
        insubdir = dirpath.lstrip(INPUT_PATH)
        outsubdir = OUTPUT_PATH + insubdir
        if not os.path.exists(outsubdir):
            os.makedirs(outsubdir)
        

        for f in filenames:
            fpath = os.path.join(dirpath, f)
            sound = AudioSegment.from_wav(fpath)
            mono_audio = sound.split_to_mono()
            outfile = os.path.join(outsubdir, f)
            mono_left = mono_audio[0].export(outfile, format='wav')

