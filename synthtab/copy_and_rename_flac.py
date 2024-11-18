import os
import shutil

in_dir = 'SynthTab_Dev/electric_muted'
out_dir = 'DemixSynthTab_Dev/electric_muted'
ext = '.flac'

for dirpath, dirnames, filenames in os.walk(in_dir):
    
    if dirpath != in_dir:

        for f in filenames:
            if ext in f:
                src = os.path.join(dirpath, f)
                dirname = dirpath.split("/")[-1]
                fname = dirname + ext
                dst = os.path.join(out_dir, fname)
                shutil.copy(src, dst)
