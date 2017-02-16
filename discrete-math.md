# Discrete math

Proving theorems:

* Test for `n = 1`
* Assume true for `m = k`
* Aim to prove true for `m = k + 1`

**Arithmetic sequence:** the difference between one term and the next is a constant.  
**Geometric sequence:** the term to term rule is to multiply or divide by the same value.

Popular sums:

* sum of `n` numbers = `n(n+1)/2` (Gauss)
* sum to `n` of `2i-1` = `i^2`
* sum to `n` `(1/2^i)` = `1`
* sum to `∞` `(1/!i)` = `e`

## Number bases

From **any base to decimal**, examples up to second power:

* **Binary (Base 2):** leading `0b`, numbers: (0, 1)  
`0b10100` = 20
(x⋅2<sup>2</sup> + y⋅2<sup>1</sup> + z⋅2<sup>0</sup>)
* **Octal (Base 8):** leading `0o`, numbers: (0, 1, 2, 3, 4, 5, 6, 7)  
`0o24` = 20
(x⋅8<sup>2</sup> + y⋅8<sup>1</sup> + z⋅8<sup>0</sup>)
* **Decimal (Base 10):** leading nothing, numbers: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)  
20 = 20
(x⋅10<sup>2</sup> + y⋅10<sup>1</sup> + z⋅10<sup>0</sup>)
* **Hexadecimal (Base 16):** leading `0x`, numbers: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)  
`0x14` = 20
(x⋅16<sup>2</sup> + y⋅16<sup>1</sup> + z⋅16<sup>0</sup>)

From **decimal to any base**, for example, five in binary:

6 / **2** = 3, **0**  
3 / **2** = 1, **1**  
1 / **2** = 0, **1**  

Solution: **6 = 0b110**

For every octal digit, we get 3 digits in binary. Because 8 = 2<sup>3</sup>.

```plaintext
  0o3 = 0b 011         = 3  
 0o13 = 0b 001 011     = 11  
0o713 = 0b 111 001 011 = 459  
```

For every hexadecimal digit, we get 4 digits in binary. Because 16 = 2<sup>4</sup>.

```plaintext
0x A 9 F C = 0b 1010 1001 1111 1100 = 43516
```

Conversion in python:

```python
decimal = int(binary, 2)
decimal = int(octal, 8)
decimal = int(hexadecimal, 16)

binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
```
