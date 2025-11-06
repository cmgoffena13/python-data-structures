# Python Data Structures

This project was created to provide detailed information and recommendations on the usage of the data structures initially available in Python.

## Hashable Python Types

A **hashable** type is one that has a hash value that never changes during its lifetime and can be compared to other objects. Hashable objects can be used as dictionary keys and set elements.

### Hashable Types (Can be dict keys / set elements)

- **Immutable built-in types**: `int`, `float`, `str`, `bytes`, `tuple`, `frozenset`
- **User-defined classes**: If they implement `__hash__()` and `__eq__()` methods
- **None**: The `None` object is hashable

### Non-Hashable Types (Cannot be dict keys / set elements)

- **Mutable built-in types**: `list`, `dict`, `set`, `bytearray`
- **Mutable user-defined classes**: By default, unless `__hash__` is explicitly set to `None`

### Why It Matters

- **Dictionary keys** must be hashable (used in hash table lookups)
- **Set elements** must be hashable (sets use hash tables internally)
- **Hashable objects** have a stable hash value that allows O(1) average lookups

### Checking if an Object is Hashable

```python
from collections.abc import Hashable

# Check if hashable
isinstance(my_object, Hashable)  # Returns True/False

# Try to hash it
try:
    hash(my_object)
    print("Hashable")
except TypeError:
    print("Not hashable")
```

### Common Gotcha

Tuples are hashable **only if all their elements are hashable**:

```python
hashable_tuple = (1, 2, 3)  # ✅ Hashable
unhashable_tuple = ([1, 2], 3)  # ❌ Not hashable (contains list)
```

## O Notation

Big O notation describes how algorithm performance scales with input size. Here are the main complexity classes:

### The Good: Efficient Complexities

- **O(1)** - Constant time: Best case. Performance doesn't change with input size (e.g., array access, dict lookup)
- **O(log n)** - Logarithmic: Excellent. Grows slowly (e.g., binary search, heap operations)
- **O(n)** - Linear: Good. Grows proportionally with input size (e.g., iterating through a list)

### The Bad: Moderate Complexities

- **O(n log n)** - Linearithmic: Acceptable. Common for efficient sorting algorithms (e.g., merge sort, quick sort)
- **O(n²)** - Quadratic: Poor. Grows quickly with nested loops (e.g., bubble sort, comparing all pairs)

### The Ugly: Inefficient Complexities

- **O(2ⁿ)** - Exponential: Terrible. Grows very fast (e.g., naive recursive Fibonacci, brute force subset generation)
- **O(n!)** - Factorial: Catastrophic. Avoid if possible (e.g., generating all permutations)

**Quick Reference:**
- Lower is better: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
- For small inputs, constants matter more than Big O
- Amortized complexity (like O(1)*) means "O(1) on average" but individual operations can be slower

## Builtin Data Structures

### List

Reference: `builtin_list.py`

|  |  | 
|----------|-------|
| Memory | O(n) |
| Add element cost | O(1) amortized (append), O(n) (insert) |
| Get element cost | O(1) (by index) |
| Data Types allowed | Any Python object |
| Mutable | Yes |
| Allows duplicates | Yes |
| Ordered | Yes |

#### Important Notes

A Python list is a very generic data structure designed for flexibility that can store any Python object / data type and modify any element. It over-allocates memory for the underlying array in anticipation of it growing. When it hits capacity, Python reallocates the underlying array with more space (typically ~1.125x growth) and copies all elements over. This is why `append()` is O(1) amortized rather than O(1) worst-case. The "Get element cost" is if you know the index, not the value itself (searching for a value is O(n)).

### Tuple

Reference: `builtin_tuple.py`

|  |  | 
|----------|-------|
| Memory | O(n) |
| Add element cost | N/A (immutable - cannot add elements) |
| Get element cost | O(1) |
| Data Types allowed | Any Python object |
| Mutable | No |
| Allows duplicates | Yes |
| Ordered | Yes |

#### Important Notes

A Python tuple cannot be modified once it is created. Slightly better memory and better performance than a list. Use in place of a list if no data modification is required.

### Dictionary

Reference: `builtin_dict.py`

|  |  | 
|----------|-------|
| Memory | O(n) |
| Add element cost | O(1) average (hash table insertion) |
| Get element cost | O(1) average (hash table lookup) |
| Data Types allowed | Keys: hashable types (str, int, tuple, etc.), Values: any Python object |
| Mutable | Yes |
| Allows duplicates | No (keys must be unique, values can duplicate) |
| Ordered | Yes |

#### Important Notes

A Python Dictionary is a good way to setup O(1) seeks on key values. 


>Note: Dictionary operations are **O(1) average** because they use hash tables. In the worst case (when all keys hash to the same bucket due to collisions), operations can degrade to **O(n)**. However, Python's hash function and load factor management ensure that in practice, dictionary operations are almost always O(1). The "average" refers to the expected performance over many operations with typical data.

### Set

Reference: `builtin_set.py`

|  |  | 
|----------|-------|
| Memory | O(n) |
| Add element cost | O(1) average (hash table insertion) |
| Membership check cost | O(1) average (hash table lookup) |
| Data Types allowed | Hashable types only (str, int, tuple, frozenset, etc.) |
| Mutable | Yes |
| Allows duplicates | No |
| Ordered | No (mathematically unordered) |

#### Important Notes

Sets hold only unique values and are optimized for exists/not exists operations. Utilize for "membership" checks and needing uniqueness of values.

### Frozen Set

Reference: `builtin_frozen_set.py`

|  |  | 
|----------|-------|
| Memory | O(n) |
| Add element cost | N/A (immutable - cannot add elements after creation) |
| Membership check cost | O(1) average (hash table lookup) |
| Data Types allowed | Hashable types only (str, int, tuple, frozenset, etc.) |
| Mutable | No |
| Allows duplicates | No |
| Ordered | No (mathematically unordered) |

#### Important Notes

Similar to a set but not modified. Is hashable so can be used as a dictionary key. Normally used instead of a set for immutability safety and hashability.

## Array Data Structure

### Array

Reference: `array_module.py`

|  |  | 
|----------|-------|
| Memory | O(n) (more memory-efficient than lists for numeric data) |
| Add element cost | O(1) amortized (append), O(n) (insert) |
| Get element cost | O(1) (by index) |
| Data Types allowed | Homogeneous numeric types only (int, float, etc. - specified by type code) |
| Mutable | Yes |
| Allows duplicates | Yes |
| Ordered | Yes |

#### Important Notes

An array is more efficient than a list. Utilize when you only need to store numeric values.

## Collections Data Structures

## HeapQ Data Structures

## Queue Data Structures