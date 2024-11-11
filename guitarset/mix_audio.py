import os
from pydub import AudioSegment

# need to change train/val depending on which dir needs processing
s1_dir = 'mix-s1s6/val/s1'
s6_dir = 'mix-s1s6/val/s6'
out_dir = 'mix-s1s6/val/mix'

for f in os.listdir(s1_dir):

    # create paths to in/out files 
    s1 = os.path.join(s1_dir, f)
    s6 = os.path.join(s6_dir, f)
    newname = f.replace('hex_cln', 'mix')
    outfile = os.path.join(out_dir, newname)

    # get the string 1 and 6 audio 
    sound1 = AudioSegment.from_file(s1)
    sound2 = AudioSegment.from_file(s6)

    # combine the audio data
    combined = sound1.overlay(sound2)

    # export the mixed audio as new wav file 
    combined.export(outfile, format='wav') 
 
