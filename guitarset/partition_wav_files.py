import os
import shutil

# directories
indir = 'mono-pickup'
outdirs = ['audio_split/train/mono-pickup', 'audio_split/val/mono-pickup']

# lists of train and val split files
splits = ['train.txt', 'val.txt']

# copy wav files to train and val directories
for i in range(len(outdirs)):
    with open(splits[i], 'r') as txtfile:
        for line in txtfile:
            fname = line.rstrip()
            fname = fname.replace('hex_cln', 'mix')
            src = os.path.join(indir, fname)
            dst = os.path.join(outdirs[i], fname) 
            shutil.copyfile(src, dst)

