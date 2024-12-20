import os
import csv
import librosa

# NEED TO MAKE TRAIN AND VAL CODE MORE COMPACT

# Change depending on the dataset!!!
SAMPLE_RATE = 44100

# CSV files
csv_train_file = 'guitarset_train.csv'
csv_val_file = 'guitarset_val.csv'

# path to the dataset
inputdir = 'dataset_s1s6'

# subdir names
mixdir_train = 'train/mix'
mixdir_val = 'val/mix'
string_1_train = 'train/s1'
string_6_train = 'train/s6'
string_1_val = 'val/s1'
string_6_val = 'val/s6'

# lists
mixture_id_train = []
mixture_id_val = []
mixture_path_train = []
mixture_path_val = []
length_train = []
length_val = []
source_1_path_train = []
source_2_path_train = []
source_1_path_val = []
source_2_path_val = []
# add list for strings 2, 3, 4, and 5 after preliminary test

# walk through the dataset and extract relevant info for csv:
# ,mixture_ID,mixture_path,source_1_path,source_2_path,length
for dirpath, dirnames, filenames in os.walk(inputdir):

    if dirpath != 'dataset':

        if mixdir_train in dirpath:
            for f in filenames:
                # append mixture id to relevant list
                mixture_id_train.append(f.strip('_mix.wav'))
                # append mixture path to relevant list
                mp = os.path.join(dirpath, f)
                mixture_path_train.append(mp)
                # append number of samples in wav to relevant list
                y, sr = librosa.load(mp, sr=SAMPLE_RATE)
                length_train.append(float(len(y)))
        
        if mixdir_val in dirpath:
            for f in filenames:
                # append mixture id to relevant list
                mixture_id_val.append(f.strip('_mix.wav'))
                # append mixture path to relevant list
                mp = os.path.join(dirpath, f)
                mixture_path_val.append(mp)
                # append number of samples in wav to relevant list
                y, sr = librosa.load(mp, sr=SAMPLE_RATE)
                length_val.append(float(len(y)))
        
        # Glean train set data
        if string_1_train in dirpath:
            for f in filenames:
                # append string 1 path to relevant list
                s1pt = os.path.join(dirpath, f)
                source_1_path_train.append(s1pt)
        if string_6_train in dirpath:
            for f in filenames:
                # append string 2 path to relevant list
                s2pt = os.path.join(dirpath, f)
                source_2_path_train.append(s2pt)
        
        # Glean val set data
        if string_1_val in dirpath:
            for f in filenames:
                # append string 1 path to relevant list
                s1pv = os.path.join(dirpath, f)
                source_1_path_val.append(s1pv)
        if string_6_val in dirpath:
            for f in filenames:
                # append string 2 path to relevant list
                s2pv = os.path.join(dirpath, f)
                source_2_path_val.append(s2pv)

# Write the train metadata to a csv file
with open(csv_train_file, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['', 'mixture_ID', 'mixture_path', 'source_1_path', 'source_2_path', 'length'])
    for i in range(len(mixture_id_train)):
        writer.writerow([i, mixture_id_train[i], mixture_path_train[i], source_1_path_train[i],
                         source_2_path_train[i], length_train[i]])

# Write the val metadata to a csv file
with open(csv_val_file, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['', 'mixture_ID', 'mixture_path', 'source_1_path', 'source_2_path', 'length'])
    for i in range(len(mixture_id_val)):
        writer.writerow([i, mixture_id_val[i], mixture_path_val[i], source_1_path_val[i],
                         source_2_path_val[i], length_val[i]])
