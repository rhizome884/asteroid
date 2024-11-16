import torch
from torch.utils.data import Dataset
import numpy as np
# import matplotlib.pyplot as plt
import os
import pandas as pd
import librosa
import random
import soundfile as sf

class GuitarSetDataset(Dataset):

    dataset_name = "GuitarSet"

    def __init__(self, csv_path, sample_rate=8000, n_src=2, segment=3):
       
        self.csv_path = csv_path
        self.segment = segment
        self.sample_rate = sample_rate

        # Open csv file
        self.df = pd.read_csv(self.csv_path)

        # Get rid of the utterances too short
        if self.segment is not None:
            max_len = len(self.df)
            self.seg_len = int(self.segment * self.sample_rate)
            # Ignore the file shorter than the desired_length
            self.df = self.df[self.df["length"] >= self.seg_len]
            print(
                f"Drop {max_len - len(self.df)} utterances from {max_len} "
                f"(shorter than {segment} seconds)"
            )
        else:
            self.seg_len = None
        self.n_src = n_src

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        # Get the row in dataframe
        row = self.df.iloc[idx]
        # Get mixture path
        mixture_path = row["mixture_path"]
        self.mixture_path = mixture_path
        sources_list = []
        # If there is a seg start point is set randomly
        if self.seg_len is not None:
            start = random.randint(0, int(row["length"] - self.seg_len))
            stop = start + self.seg_len
        else:
            start = 0
            stop = None
        # Read sources
        for i in range(self.n_src):
            source_path = row[f"source_{i + 1}_path"]
            s, _ = sf.read(source_path, dtype="float32", start=start, stop=stop)
            sources_list.append(s)
        # Read the mixture
        mixture, _ = sf.read(mixture_path, dtype="float32", start=start, stop=stop)
        # Convert to torch tensor
        mixture = torch.from_numpy(mixture)
        # Stack sources
        sources = np.vstack(sources_list)
        # Convert sources to tensor
        sources = torch.from_numpy(sources)
        return mixture, sources

if __name__ == "__main__":

    # create the train and validation paths
    train_path = "./dataset_s1s6_8kHz/metadata/train.csv"
    # val_path = "guitarset_s1s6_8kHz/metadata/val.csv"
    
    # instantiate GuitarSetDataset object(s)
    train_set = GuitarSetDataset(train_path)
    item = train_set.__getitem__(0)
    print(len(item))
    
