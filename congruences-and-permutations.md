# Congruences

`a` is congruent to `b mod n` if `n` divides `(a-b)` i.e. if there is an integer `k` such that `a-b = k*n`.

a = b (mod n)

```python
print((a - b) % n == 0)
```

* **reflexive property:** a is congruent to a mod n.

* **symmetric property:** if a is congruent to b mod n, then b is congruent to a mod n.

* **transitive property:** if a is congruent to b mod n and b is congruent to c mod n, then a is congruent to c mod n:

(a - b) + (b - c) = n(k + m)

```python
# if:
(a - b) % n == 0
# and:
(b - c) % n == 0
# then:
(a - c) % n == 0
```

Caesar encryption:

```python
SPACE = ' '

def encrypt(letter, positions):
    if letter == SPACE: return SPACE
    return chr((ord(letter) + positions - 97) % 26 + 97)

message = 'hello world'
print(''.join(encrypt(letter, 3) for letter in message))
```


# Enumeration

* If you find yourself saying "or", you have to add.
* If you find yourself saying "and" or "for every", you have to multiply.

## Enumerations

When `n` different events can occur in `m` independent ways, there are **n<sup>m</sup>** possible combinations. Also if you can pick `m` options out of `n` possible choices with repetition allowed.

Example: picking 3 ice-cream flavours out of 10: 10<sup>3</sup> = 1000 ways to do it.


## Permutations

Arranging `n` items without repetition results in `n!` permutations.  
Order matters.

Example: how many ways could `n` books be placed on a shelf. How many ways to arrange any `n` cards from a deck.

Rules:

* `0! = 1`
* The factorial operation is undefined for numbers less than zero.


### Permutations of a subset

If you pick a selection of `m` of the `n` possible options, then it's:

`P(n, m) = n! / (n - m)!`  

Example: how many ways could you be dealt `m` unsorted cards from a `n`-card deck.

### Permutations of a multiset

Multiset: set with identical items. We scale `n!` by `m!`.

`P(n; m1, m2...) = n! / m1! m2! ...`

Example: what's the number of permutations of the word CODEC: C<sub>1</sub>ODEC<sub>2</sub> =  C<sub>2</sub>ODEC<sub>1</sub> so `5! / 2!`


## Combinations

Order doesn't matter. Reduces number of combinations as some are the same.

`C(n, k) = (n k) = n! / k!(n - k)!`

Example: Picking 3 numbers: 1, 2, 3 = 3, 2, 1 etc. How many different `m`-card hands can you have out of a deck of `m` cards.

Rules:

* `C(n, n) = 1`
* `C(n, 1) = n`

### Selecting items from a multiset

Example: How many ways to order 8 of 3 different tacos.

* If order matters: 3<sup>8</sup>.
* If it doesn't: xx|xxxx|xx or xxx|xxx|xx, etc. We have `n - 1` delimiters, `n` tacos, `k` tacos to order and (`k` + delimiters) positions to combine.

`C(k + n - 1, k) = (k + n - 1)! / k! (n - 1)`

### Element composition

How many permutations of the word APPLE in which the two P's are next to one another?

Consider `PP` a letter. S = { A, PP, L, E } = 4! = 24
