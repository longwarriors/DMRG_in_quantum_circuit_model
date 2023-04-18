import torch
import numpy as np
from torch import tensor 
from numpy import array

class Hamiltonian:
    Fermion_Sz = tensor([
        [1., 0.],
        [0., -1]
    ],dtype=torch.cfloat) / 2

    Boson_Sz = tensor([
        [1., 0, 0],
        [0., 0, 0],
        [0, 0, -1]
    ],dtype=torch.cfloat)

if __name__ == "__main__":
    print(torch.linalg.eigh(Hamiltonian.Boson_Sz))