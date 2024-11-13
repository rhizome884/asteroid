import torch
from torch.utils.data import Dataset
# import matplotlib.pyplot as plt
import os
import pandas as pd
import librosa

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

if __name__ == "__main__":

    # create the train and validation paths
    train_path = "guitarset_s1s6_8kHz/metadata/train.csv"
    # val_path = "guitarset_s1s6_8kHz/metadata/val.csv"
    
    # instantiate GuitarSetDataset object(s)
    train_set = GuitarSetDataset(train_path)

