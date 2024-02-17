import torch
import numpy as np


class CustDataset(torch.utils.data.Dataset):
    def __init__(self, x, y, labels):
        self.x = np.array(x)
        self.y = np.array(y)
        self.z = np.array(labels)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        data = np.array(
            [self.x[idx].astype(np.float32), self.y[idx].astype(np.float32)]
        )
        label = np.array(self.z[idx].astype(np.float32))
        return data, label
