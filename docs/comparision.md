# Algorithm Performance Summary

| Algorithm             | Time Complexity (Best) | Time Complexity (Avg) | Time Complexity (Worst) | Space Complexity | Observed Execution Time Trend | Observed Memory Usage Trend | Notes                       |
| --------------------- | ---------------------- | --------------------- | ----------------------- | ---------------- | ----------------------------- | --------------------------- | --------------------------- |
| Fibonacci (Recursive) | O(2^n)                 | O(2^n)                | O(2^n)                  | O(n)             | Exponential growth            | High due to recursion stack | Risk of stack overflow      |
| Fibonacci (DP)        | O(n)                   | O(n)                  | O(n)                    | O(n)             | Linear scaling                | Stable, moderate            | Much faster than recursive  |
| Merge Sort            | O(n log n)             | O(n log n)            | O(n log n)              | O(n)             | Smooth n log n growth         | Moderate due to merging     | Stable & efficient          |
| Quick Sort            | O(n log n)             | O(n log n)            | O(n^2)                  | O(log n)         | Very fast in average cases    | Low                         | Worst case on sorted data   |
| Insertion Sort        | O(n)                   | O(n^2)                | O(n^2)                  | O(1)             | Fast for small inputs         | Very low                    | Best for nearly sorted data |
| Bubble Sort           | O(n)                   | O(n^2)                | O(n^2)                  | O(1)             | Slow growth after small input | Very low                    | Inefficient for large data  |
| Selection Sort        | O(n^2)                 | O(n^2)                | O(n^2)                  | O(1)             | Predictably quadratic         | Very low                    | Rarely used in practice     |
| Binary Search         | O(1)                   | O(log n)              | O(log n)                | O(1)             | Very fast, logarithmic trend  | Negligible                  | Requires sorted data        |
