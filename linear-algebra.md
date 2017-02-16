# Linear algebra

## Vectors

Norm: **|v| = √sum(v<sub>i</sub><sup>2</sup>)**

```python
v = np.array([2, -4, 1])
v_norm = np.linalg.norm(v)
```


### Dot product

ab = ba

**ab = sum(a<sub>i</sub>b<sub>i</sub>)**  
**ab = |a| |b| cosθ** => allows to get θ

Result is a scalar.  
Is zero for perpendicular vectors (**cos90 = 0**).

```python
u = np.array([-1, -2, -3])
v = np.array([2, 2, 2])

product = np.dot(u, v)
```

### Cross product

**ab = sum(a<sub>i</sub>b<sub>i</sub>)**  
**axb = |a| |b| senθ**

Result is a vector.  
Is zero for parallel vectors (**sen0 = 0**).

```python
u = np.array([-1, -2, -3])
v = np.array([2, 2, 2])

product = np.cross(u, v)
```


## Matrices

```python
M = np.array([[1, 2], [3, 4]])
```

or

```python
v = np.array([2, 2, 2])
u = np.array([0, 0, 0])
w = np.array([3, 3, 3])

M = np.column_stack((v, u, w))
```

```python
M.shape
M[0, 1]
M[:, 1]
```

```python
M = np.array([[1, 2], [3, 4]])

product = 4 * M
```

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[-4, -3], [-2, -1]])

sum = A + B
```


### Identity Matrix

Multiplying a matrix by the identity gives the original matrix.  
**MI = M**

```plaintext
    |1 0 0|   
I = |0 1 0|
    |0 0 1|
```

```python
identity = np.eye(4)
```

```python
zeros = np.zeros((5))
zeros = np.zeros((3, 2))
```

### Transpose matrix

Swaps rows with columns: **M<sup>T</sup>**

```python
M = np.array([[1, 2], [3, 4]])
transposed = M.T
```

### Permutation matrix

Swap rows or swap columns.  
We swap the identity column or row we want to swap in the original matrix.

```plaintext
    |0 1 0|
P = |0 0 1|
    |1 0 0|
```
* Swap columns: **MP**
* Swap rows: **PM**


### Inverse matrix

We can not divide matrices, but we can multiply by the inverse.

**MM<sup>−1</sup> = M<sup>−1</sup>M = I**

xA = BC ==> x = BCA<sup>−1</sup>

```python
M = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(M)
```


### Singular Matrix

A matrix that does not have an inverse.


### Dot product

AB ≠ BA

Dot product of rowsA by colsB, Condition: **rowsA = colsB**.  
Resulting matrix shape is **colsA x rowsB**.

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[-4, -3], [-2, -1]])

product = np.matmul(A, B)

# or:
product = A@B
```

## Gauss-Jordan Elimination


### Row echelon (matriz escalonada)

```
| a b c | |x| = |d1|     | 1 b' c' | d1' |
| d e f | |y| = |d2| ==> | 0 1  f' | d2' |
| g h i | |z| = |d3|     | 0 0  1  | d3' |
```

First we add or subtract rows, multiplied by any relevant quantity, in order to get the zeros. We can also swap rows as needed. Finally, we multiply the rows as needed to normalize them (to get the ones).

If the system of equations has no solution, we won't be able to do a row echelon.

```python
#  x + 4y -  z = -1
# -x - 3y + 2z =  2
# 2x -  y - 2z = -2

M = np.array([[1, 4, -1], [-1, -3, 2], [2, -1, -2]])
d = np.array([-1, 2, -2])

x, y, z = np.linalg.solve(M, d)
```

We can also use Gauss-Jordan elimination to find the inverse matrix:

M | I => GJE => I | M<sup>−1</sup>

## Next
* [Cheatsheet](https://www.codecademy.com/learn/learn-linear-algebra/modules/math-ds-linear-algebra/cheatsheet)
