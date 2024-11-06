from pydub import AudioSegment
import os

def split_to_mono(file_path):
    # takes path to multichannel wav file, 
    # splits file to mono, then returns array of pydub sound objects
    file = AudioSegment.from_wav(file_path)
    multichan = file.split_to_mono()
    return multichan

# Directory names
INPUT_DIR = "audio_hex-pickup_debleeded"
OUTPUT_DIR = "audio_split"
SPLIT_DIRS = ['train', 'val']
STRING_DIRS = ['s1', 's2', 's3', 's4', 's5', 's6']

# Train/validation split filenames
splits = ['train.txt', 'val.txt']

# Make output dir
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Make output subdirs
for tts in SPLIT_DIRS:
    tts_path = os.path.join(OUTPUT_DIR, tts)
    if not os.path.exists(tts_path):
        os.makedirs(tts_path)
    for sd in STRING_DIRS:
        sd_path = os.path.join(tts_path, sd)
        if not os.path.exists(sd_path):
            os.makedirs(sd_path)

for split in splits:
    with open(split, 'r') as txtfile:
        for line in txtfile:
            wavpath = os.path.join(INPUT_DIR, line.rstrip())
            channels = split_to_mono(wavpath)
            
            # create guitar string var (channel 0 = string 6) for filenaming
            gtrstr = 6

            # export the individual hex string audio to corresponding subdirectory
            for channel in channels:
                string_fldr = 's' + str(gtrstr)
                outfile = os.path.join(OUTPUT_DIR, split.split('.')[0], string_fldr, line.rstrip())
                channel.export(outfile, format='wav')
                gtrstr -= 1
                

#for f in os.listdir(INPUT_PATH):
#    
#    # load multichannel file and split into 6 mono sound objects
#    file_path = os.path.join(INPUT_DIR, f)
#    file = AudioSegment.from_wav(file_path)
#    multichan = file.split_to_mono()
#
#    # create guitar string var (channel 0 = string 6) for filenaming
#    gtrstr = 6
#    
#    # save the six sound objects as wav files
#    for chan in multichan:
#        filename = f.split('.')[0] + '_' + str(gtrstr) + '.' + f.split('.')[-1]
#        chan.export(OUTPUT_DIR + filename, format='wav')
#        gtrstr -= 1
