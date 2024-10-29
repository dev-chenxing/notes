# 线性方程组

## 齐次线性方程组

方程组
\[\begin{align*}
  a_{11}x_1+a_{12}x_2+\dots&+a_{1n}x_n = 0 \\
  a_{21}x_1+a_{22}x_2+\dots&+a_{2n}x_n = 0 \\
  \dots & &(\text{I})\\
  a_{m1}x_1+a_{m2}x_2+\dots&+a_{mn}x_n = 0
\end{align*}\]
称为$m$个方程，$n$个未知量的齐次线性方程组.
其矩阵形式为
\[A_{m\times n}x=0.\]

### 有解的条件

**齐次线性方程组有解的条件** 当$r(A)=n$（$\alpha_1, \alpha_2, \dots, \alpha_n$线性无关）时，方程组(I)有唯一解；当 $r(A)=r<n$（$\alpha_1, \alpha_2, \dots, \alpha_n$线性相关）时，方程组(I)有无穷多解.

未知数个数大于方程个数，必有非零解.
