import os
import csv
import librosa

# Change depending on the dataset!!!
SAMPLE_RATE = 8000

# path to the dataset
inputdir = 'dataset_downsample'

# subdir names
mixdir = 'mono-pickup'
string_1 = 's1'
string_6 = 's6'

# lists
mixture_id = []
mixture_path = []
source_1_path = []
source_2_path = []
length = []
# add list for strings 2, 3, 4, and 5 after preliminary test

# walk through the dataset and extract relevant info for csv:
# ,mixture_ID,mixture_path,source_1_path,source_2_path,length
for dirpath, dirnames, filenames in os.walk(inputdir):
    if dirpath != 'dataset':
        if mixdir in dirpath:
            for f in filenames:
                # append mixture id to relevant list
                mixture_id.append(f.strip('_mix.wav'))
                # append mixture path to relevant list
                mp = os.path.join(dirpath, f)
                mixture_path.append(mp)
                # append number of samples in wav to relevant list
                y, sr = librosa.load(mp, sr=SAMPLE_RATE)
                length.append(float(len(y)))

        if string_1 in dirpath:
            for f in filenames:
                # append string 1 path to relevant list
                s1p = os.path.join(dirpath, f)
                source_1_path.append(s1p)
        if string_6 in dirpath:
            print(dirpath)
            for f in filenames:
                # append string 2 path to relevant list
                s2p = os.path.join(dirpath, f)
                source_2_path.append(s2p)

# Write the metadata to a csv file
