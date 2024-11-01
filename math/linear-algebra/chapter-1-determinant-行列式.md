# 第1讲 行列式

## 行列式的本质定义（第一种定义）

$n$阶行列式$D_n=\begin{vmatrix}
     a_{11} & \dots & a_{1n}\\ 
     \vdots &  & \vdots\\
     a_{31} & \dots & a_{3n} 
\end{vmatrix}$的本质定义：
$\bf n(n\geq3)$**阶行列式是由**$\bf n$**个**$\bf n$**维向量**$\alpha_1=[a_{11}, a_{12}, \dots, a_{1n}],\alpha_2=[a_{21}, a_{22}, \dots, a_{2n}],\dots,\alpha_n=[a_{n1}, a_{n2}, \dots, a_{nn}]$**组成的，其（运算规则的）结果为以这**$\bf n$**个向量为邻边的**$\bf n$**维图形的体积**. 
若$D_n\neq0$，则意味着体积不为0，则称组成该行列式的$n$个向量**线性无关**；若$D_n\neq0$，则称**线性相关**.

## 几个重要的行列式

### 范德蒙德行列式

**范德蒙德行列式** \[\begin{vmatrix}
     1 & 1 & \dots & 1\\ 
     x_1 & x_2 & \dots & x_n \\
     x_1^2 & x_2^2 & \dots & x_n^2 \\
     \vdots & \vdots &  & \vdots \\
     x_1^{n-1} & x_2^{n-1} & \dots & x_n^{n-1}
\end{vmatrix}=\prod_{1\leq i<j\leq n}(x_j-x_i).\]
