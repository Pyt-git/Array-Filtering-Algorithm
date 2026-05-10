# Array-Filtering-Algorithm
This repository contains a custom single-pass array filtering algorithm implemented in Python. The function removes elements from a list of dictionaries based on a specified key-value condition while iterating through the list only once. 

How the algorithm works: 
- Function scans the list from left to right using an index
- When an element matches the condition, it is removed in place; otherwise, the index advances
- Ensures that each element is examined at least once

Time Compolexity: 
- Algorithmic complexity: O(n). The algorithm performs a single logical pass over the list, and each element is visited at most once
- Python implementation note: Because Python lists require shifting elements when pop(i) is used, the actual runtime in CPython behaves much closer to O(n^2)
- The algorithm remains O(n) in a language-agnostic sense

Unit tests:
The repository includes a unittest test suite covering: 

- Removal of matching elements
- Cases with no matches
- Empty lists
- Single-element lists

These tests validate correctness and edge case behavior.

Use cases: 
This algorithm is useful when: 

- You need to filter structured data (eg, dictionaries)
- You want to avoid creating a second list
- You prefer an in-place, single-pass approach
