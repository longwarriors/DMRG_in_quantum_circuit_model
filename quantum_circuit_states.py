"""
A quantum state in the Hilbert space spanned by computational bases is a vector of the projected components.
"""

import torch
from torch import tensor
from numpy import sqrt, diag, ravel_multi_index


def kron_mat(*matrices, arch="cpu"):
    res = torch.eye(1.0, device=arch)  # eye(1).shape=(1,1)
    for mat in matrices:
        a, b = res.shape
        c, d = mat.shape
        res = torch.einsum("ab,cd->acbd", res, mat).reshape(a * c, b * d)
    return res


def kron_vec(*vectors, arch="cpu"):
    res = torch.tensor([1.0], device=arch)  # res.shape=(1,)
    for v in vectors:
        res = torch.einsum("a,b->ab", res, v).flatten()  # 降维成一维向量
    return res


def rand_state(N: int = 1, arch="cpu"):
    # Yao.rand_state(n)
    state = torch.randn(size=(2**N,), dtype=torch.cfloat, device=arch)
    state /= state.norm()  # normalization
    return state


def rand_separable_state(N: int = 1, arch="cpu"):
    # Tensor product of normalized vectors is still normalized,
    # No need to re-normalize the result.
    separable = (rand_state(1, arch) for _ in range(N))
    return kron_vec(*separable, arch=arch)  # *tuple是对元组解包


def entangled_Bell(k_th: int = 0, arch="cpu"):
    ########## ↓↓↓ Spin triplet states ↓↓↓ ##########
    # $\phi+$
    phi_0 = tensor([1 / sqrt(2), 0, 0, 1 / sqrt(2)], dtype=torch.cfloat, device=arch)
    # $\phi-$
    phi_1 = tensor([1 / sqrt(2), 0, 0, -1 / sqrt(2)], dtype=torch.cfloat, device=arch)
    # $\psi+$
    psi_0 = tensor([0, 1 / sqrt(2), 1 / sqrt(2), 0], dtype=torch.cfloat, device=arch)
    ########## ↑↑↑ Spin triplet states ↑↑↑ ##########

    ########## ↓↓↓ Spin singlet state  ↓↓↓ ##########
    # $\psi-$
    psi_1 = tensor([0, 1 / sqrt(2), -1 / sqrt(2), 0], dtype=torch.cfloat, device=arch)
    ########## ↑↑↑ Spin singlet state  ↑↑↑ ##########

    overall = [phi_0, phi_1, psi_0, psi_1]
    return overall[k_th]


def entangled_GHZ(N: int = 3, arch="cpu"):
    state = torch.zeros(2**N, dtype=torch.cfloat, device=arch)
    state[0], state[-1] = 1 / sqrt(2), 1 / sqrt(2)
    return state


def entangled_W(N: int = 3, arch="cpu"):
    binary_indices = diag((1,) * N)
    # Converts index arrays into an array of flat indices
    decimal_indices = ravel_multi_index(binary_indices, dims=(2,) * N)
    coeff = 1 / sqrt(N)
    state = torch.zeros(2**N, dtype=torch.cfloat, device=arch)
    state[decimal_indices] = coeff
    return state


if __name__ == "__main__":
    torch.cuda.empty_cache()  # 计算前清空GPU cache
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("Random state: \n", rand_state(3, arch=device))
    print("Separable state: \n", rand_separable_state(3, arch=device))
    print("Bell state: \n", entangled_Bell(2, arch=device))
    print("GHZ state: \n", entangled_GHZ(4, arch=device))
    print("W state: \n", entangled_W(4, arch=device))
