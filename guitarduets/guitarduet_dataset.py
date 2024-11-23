import torch
from torch.utils.data import Dataset
import numpy as np
import os
import pandas as pd
import librosa
import random
import soundfile as sf

class GuitarDuetDataset(Dataset):

    dataset_name = "GuitarDuet"

    def __init__(self, csv_path, sample_rate=16000, n_src=2, segment=3):
       
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
                f"Drop {max_len - len(self.df)} sounds from {max_len} "
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
            s = self._cut_if_necessary(s)
            s = self._right_pad_if_necessary(s)
            sources_list.append(s)
        # Read the mixture
        mixture, _ = sf.read(mixture_path, dtype="float32", start=start, stop=stop)
        mixture = self._cut_if_necessary(mixture)
        mixture = self._right_pad_if_necessary(mixture)
        # Convert to torch tensor
        mixture = torch.from_numpy(mixture)
        # Stack sources
        sources = np.vstack(sources_list)
        # Convert sources to tensor
        sources = torch.from_numpy(sources)
        return mixture, sources

    def _cut_if_necessary(self, signal):
        # signal -> tensor -> (channels, number of samples)
        if signal.shape[0] > self.seg_len:
            signal = signal[:self.seg_len]
        return signal

    def _right_pad_if_necessary(self, signal):
        length_signal = signal.shape[0]
        if length_signal < self.seg_len:
            num_missing_samples = self.seg_len - length_signal
            last_dim_padding = (0, num_missing_samples)
            signal = torch.nn.functional.pad(torch.from_numpy(signal), last_dim_padding)
        return signal
 
