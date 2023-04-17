# DMRG_in_quantum_circuit_model  

***DMRG is useful for physical researchers to cross the threshold of quantum computing.***   

## 量子多体格点模型与量子线路模型  

&emsp;&emsp;量子线路模型是用量子比特张开希尔伯特空间，并施加量子逻辑门对量子态进行酉变换的操作。波函数是complex Hilbert空间中的向量 $\vec{\psi}$，在量子多体问题中，复合系统希尔伯特空间是子系统希尔伯特空间的张量积。  

$$
\hat{e}\left(\underbrace{●●●●●●●●●●}_N\right) = \bigotimes_{i=1}^{N}\hat{s_i} = \ket{s_1,s_2,\dots,s_N}
$$

&emsp;&emsp;格点模型（lattice sites）的希尔伯特空间，先从单个点粒子自旋  $\hat s_i$  的基态入手。费米子（Fermionic）的电子基态为2个：自旋向上 $\ket{m_s=\frac{1}{2}}=\ket{\uarr}=[1,0]^T$ ，自旋向下 $\ket{m_s=-\frac{1}{2}}=\ket{\darr}=[0,1]^T$ ，在量子计算中被称为qubit ；玻色子（Bosonic）的光子基态为3个 $[ |-1 \rangle, |0 \rangle, |+1 \rangle ]$ ，在量子计算中被称为qutrit

&emsp;&emsp;根据量子力学[四大公理](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.126.110402)，格点系统的基态波函数是一系列单体波函数的直积态。  

量子态   

$$\begin{aligned}
\vec{\psi} &= \begin{pmatrix} \vert \\ \psi_i \\ \vert \\ \end{pmatrix} \in \Bbb{C}^{L \times 1} \\ 
\vec{\psi}^\dagger &= \begin{pmatrix} \text{---} \hspace{-0.2cm} & \psi_i^* & \hspace{-0.2cm} \text{---} \end{pmatrix} \in \Bbb{C}^{1 \times L} 
\end{aligned}$$