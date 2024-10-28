# 第 3 讲 向量组

## 向量与向量组的线性相关性

### 向量组的线性表示与线性相关的概念

**线性表示** 若向量$\beta$能表示成向量组$\alpha_1, \alpha_2, \dots, \alpha_m$的线性组合，即存在$m$个数$k_1, k_2, \dots, k_m$，使得\[\beta=k_1\alpha_1+k2\alpha_2+\dots+k_m\alpha_m,\]则称向量$\beta$能被向量组$\alpha_1, \alpha_2, \dots, \alpha_m$线性表示.

**线性相关** 对于$m$个$n$维向量$\alpha_1, \alpha_2, \dots, \alpha_m$，若存在一组不全为零的数$k_1, k_2, \dots, k_m$，使得\[k_1\alpha_1+k2\alpha_2+\dots+k_m\alpha_m=0,\]则称向量组$\alpha_1, \alpha_2, \dots, \alpha_m$线性相关.

**线性无关** 若不存在不全为零的数$k_1, k_2, \dots, k_m$，使得$k_1\alpha_1+k2\alpha_2+\dots+k_m\alpha_m=0$成立，则称向量组$\alpha_1, \alpha_2, \dots, \alpha_m$线性无关.

向量组或线性相关或线性无关，二者必居其一且仅居其一.

### 判别线性相关性的七大定理

*定理4* 设$m$个$n$维向量$\alpha_1, \alpha_2, \dots, \alpha_m$，其中\[\alpha_1=[a_{11}, a_{21}, \dots, a_{n1}]^T,\]\[\alpha_2=[a_{12}, a_{22}, \dots, a_{n2}]^T,\]\[\dots\]\[\alpha_m=[a_{1m}, a_{2m}, \dots, a_{nm}]^T.\]向量组$\alpha_1, \alpha_2, \dots, \alpha_m$线性相关$\lrArr$齐次线性方程组\[[\alpha_1, \alpha_2, \dots, \alpha_m]\begin{bmatrix}x_{1}\\x_{2}\\\vdots\\x_{m}\end{bmatrix}=x_1\alpha_1+x_2\alpha_2+\dots+x_m\alpha_m=0\]有非零解 $\lrArr r(\alpha_1, \alpha_2, \dots, \alpha_m)<m$