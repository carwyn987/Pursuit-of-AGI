#!../../p39/bin/python

"""
Generates simple two integer multiplication data

Call the program with N as a cmdline argument. With N = 2, from WITHIN the neural_encoded_multiplication/ folder:
```
$ python multiplication_data_generator.py 2
```
or
```
./multiplication_data_generator.py 2
```
"""

import sys
import numpy as np
from tqdm import tqdm
import torch


def multiplication_data_generator(N, write=False, symmetric=True):
    """
    Generates multiplication data in the form:

    Example (Note, header not written ever):

    x | y | x * y (label)
    -------------
    0 | 0 | 0
    0 | 1 | 0
    1 | 0 | 0
    1 | 1 | 1
    1 | 2 | 2

    Arguments:
    -------------
        N (int): Defines range of x and y as [0,N-1] (a.k.a. inclusive).
        write (bool): Whether to write to file. If true, writes data to "../../data/addition_data.csv". Else, returns list of tuples in form (x,y,x+y)
        symmetric (bool): If true, writes from [-N+1, N-1] rather than [0,N-1]. Is a modifier (overrides specification) for N.

    Returns:
    -------------
        data (list): If write is false, returns the dataset as a list of tuples (x,y,x+y).
    """

    print("Generating Data ...")

    # Conditional outside loop for efficiency
    if write:
        with open("../../data/multiplication_data.csv", "w") as f:
            for x in tqdm(range(-N + 1, N) if symmetric else range(N)):
                for y in range(-N + 1, N) if symmetric else range(N):
                    f.write(str(x) + "," + str(y) + "," + str(x * y) + "\n")
        return
    else:
        data = []
        for x in tqdm(range(-N + 1, N) if symmetric else range(N)):
            for y in range(-N + 1, N) if symmetric else range(N):
                data.append((x, y, x * y))
        return data


if __name__ == "__main__":
    # Argument parsing should use "argparse" or "absl" (Google designed argparser) for more reliability.
    N = sys.argv[1]
    symmetric = bool(sys.argv[2] if len(sys.argv) > 2 else True)
    multiplication_data_generator(int(N), write=True, symmetric=symmetric)


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
