import os
from sklearn.model_selection import train_test_split

dirname = 'audio_hex-pickup_debleeded'
files = []

for f in os.listdir(dirname):
    files.append(f)

train, val = train_test_split(files, test_size=0.2)

splits = [train, val]
fnames = ['train.txt', 'val.txt']

for i in range(len(splits)):
    with open(fnames[i], 'w', encoding='UTF-8') as outfile:
        for item in splits[i]:
            outfile.write(item + '\n')
