import os
import csv
import librosa

# path to the dataset
inputdir = 'dataset'

# subdir names
mixdir = 'mono-pickup'

# lists
mixture_id = []
mixture_path = []
s1 = []
s2 = [] 
# add list for strings 3, 4, 5, and 6 after preliminary test
length = []

# walk through the dataset and extract relevant info for csv:
# ,mixture_ID,mixture_path,source_1_path,source_2_path,length
for dirpath, dirnames, filenames in os.walk(inputdir):
    if dirpath != 'dataset':
        for f in filenames:
            # append mixture id to relevant list
            mixture_id.append(f.strip('.wav'))

print(mixture_id)
