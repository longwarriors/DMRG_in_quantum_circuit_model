import torch
import numpy as np
from torch import tensor 
from numpy import array

class Hamiltonian:
    """对称矩阵和厄密矩阵的本征值都是实数"""
    
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
    val, vec = torch.linalg.eigh(Hamiltonian.Fermion_Sz)
    spin_up_eigenvalue = val[1] # 1/2
    spin_down_eigenvalue = val[0] # -1/2
    spin_up_eigenvector = vec[:,1]
    spin_down_eigenvector = vec[:,0]
    
    print(val)
    print(vec)