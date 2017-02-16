# Sets

A set is unordered and unindexed.

Universe: die numbers: {1, 2, 3, 4, 5, 6}

Two sets:

* A = {1, 3, 5} (odd)
* B = {3, 4, 5, 6} (> 2)

## Operations

### Union

`A || B`
Any element that exists in either A, B or both.

A ∪ B = {1, 3, 4, 5, 6}.


### Intersection  

`A && B`
Any element that exists in both of the sets.

A ∩ B = {3, 5}.


### Complement

`!A`
All possible outcomes outside of the set.

A' = {2, 4, 6}


## Rules

* Identity Property for Union: A ∪ ∅ = A.
* Identity Property for Intersection: A ∩ U = A.
* Domination Law 1: A ∩ ∅ = ∅.
* Domination Law 2: A ∪ U = U.


## In python

To create an empty set in Python, use `set()`, not `{}`. The latter creates an empty dictionary.

* `A.issubset(B)` checks if one set is a subset of another.
* `A.difference(B)` returns a set that contains the items that only exist in one set and not the other.
* `A.len()` returns cardinality (total items in set). If `A = {1, 3, 0, 7, 9}` then `|A| = 5`.
* `A.intersection(B)` and `A.union(B)` too
