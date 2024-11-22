import os
import shutil

in_dir = 'RealTest'
out_dir = 'real_test'
sub_dir_g1 = 'guitar1'
sub_dir_g2 = 'guitar2'
sub_dir_mix = 'mix'

sub_dirs = [sub_dir_g1, sub_dir_g2, sub_dir_mix]

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

for sub_dir in sub_dirs:
    sub_dir_path = os.path.join(out_dir, sub_dir)
    if not os.path.exists(sub_dir_path):
        os.makedirs(sub_dir_path)

ext = '.wav'

for dirpath, dirnames, filenames in os.walk(in_dir):
    
    if dirpath != in_dir:

        for f in filenames:
            if ext in f:
                src = os.path.join(dirpath, f)
                dirname = dirpath.split("/")[-1]
                fname = dirname + "_" + f
                if f == 'guitar1.wav': 
                    dst = os.path.join(out_dir, sub_dir_g1, fname)
                    shutil.copy(src, dst)
                elif f == 'guitar2.wav': 
                    dst = os.path.join(out_dir, sub_dir_g2, fname)
                    shutil.copy(src, dst)
                else:
                    dst = os.path.join(out_dir, sub_dir_mix, fname)
                    shutil.copy(src, dst)
