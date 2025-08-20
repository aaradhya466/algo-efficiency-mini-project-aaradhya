# Algorithm Analysis Documentation

## 1. Fibonacci Sequence

### Naïve Recursive Approach

- **Input:** Integer `n`
- **Output:** `n`-th Fibonacci number
- **Time Complexity:**

  - Best: O(2^n)
  - Average: O(2^n)
  - Worst: O(2^n)

- **Space Complexity:** O(n) (due to recursion stack)
- **Suitability and Trade-offs:**

  - Very simple to implement.
  - Extremely inefficient for large `n` because of repeated calculations.

### Dynamic Programming (Memoization / Tabulation)

- **Input:** Integer `n`
- **Output:** `n`-th Fibonacci number
- **Time Complexity:**

  - Best: O(n)
  - Average: O(n)
  - Worst: O(n)

- **Space Complexity:**

  - O(n) (with memoization)
  - O(1) (with iterative tabulation and two variables)

- **Suitability and Trade-offs:**

  - Much faster than recursion.
  - Slight trade-off: requires extra memory for storing intermediate values.

---

## 2. Merge Sort

- **Input:** Array of size `n`
- **Output:** Sorted array
- **Time Complexity:**

  - Best: O(n log n)
  - Average: O(n log n)
  - Worst: O(n log n)

- **Space Complexity:** O(n) (extra space for merging)
- **Suitability and Trade-offs:**

  - Very efficient for large datasets.
  - Stable sorting algorithm.
  - Requires extra space → not suitable for memory-constrained systems.

---

## 3. Quick Sort

- **Input:** Array of size `n`
- **Output:** Sorted array
- **Time Complexity:**

  - Best: O(n log n) (when pivots are balanced)
  - Average: O(n log n)
  - Worst: O(n²) (when array is already sorted or pivot choice is poor)

- **Space Complexity:** O(log n) (for recursion stack, in-place sort)
- **Suitability and Trade-offs:**

  - Faster than Merge Sort in practice (better cache performance).
  - In-place, so uses less memory.
  - Not stable by default.
  - Performance highly depends on pivot selection.

---

## 4. Insertion Sort

- **Input:** Array of size `n`
- **Output:** Sorted array
- **Time Complexity:**

  - Best: O(n) (already sorted input)
  - Average: O(n²)
  - Worst: O(n²)

- **Space Complexity:** O(1) (in-place)
- **Suitability and Trade-offs:**

  - Excellent for small datasets.
  - Adaptive (fast for nearly sorted arrays).
  - Not suitable for large datasets.

---

## 5. Bubble Sort

- **Input:** Array of size `n`
- **Output:** Sorted array
- **Time Complexity:**

  - Best: O(n) (if optimized with a flag for early stop)
  - Average: O(n²)
  - Worst: O(n²)

- **Space Complexity:** O(1) (in-place)
- **Suitability and Trade-offs:**

  - Very simple but extremely inefficient for large datasets.
  - Rarely used in real-world applications.
  - Good for teaching sorting basics.

---

## 6. Selection Sort

- **Input:** Array of size `n`
- **Output:** Sorted array
- **Time Complexity:**

  - Best: O(n²)
  - Average: O(n²)
  - Worst: O(n²)

- **Space Complexity:** O(1) (in-place)
- **Suitability and Trade-offs:**

  - Simpler than other sorts.
  - Performance is consistently poor for large datasets.
  - Not stable.

---

## 7. Binary Search

- **Input:** Sorted array of size `n`, target element `x`
- **Output:** Index of `x` if found, otherwise -1
- **Time Complexity:**

  - Best: O(1) (middle element is the target)
  - Average: O(log n)
  - Worst: O(log n)

- **Space Complexity:**

  - O(1) (iterative)
  - O(log n) (recursive, due to stack)

- **Suitability and Trade-offs:**

  - Very efficient for searching in sorted datasets.
  - Requires sorted input.
  - Not useful for unsorted arrays.

---
