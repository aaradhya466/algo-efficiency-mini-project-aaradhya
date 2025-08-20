# Reflections on Experimental Profiling

1. **Fibonacci Recursive vs DP**

   - Expected: Recursive is exponential, DP is linear.
   - Observed: Recursive became impractical beyond n=35 (long runtime, stack overflow risk). DP handled n=10^6 efficiently.

2. **Sorting Algorithms**

   - Merge Sort behaved consistently with O(n log n).
   - Quick Sort was faster than Merge Sort for most random inputs but degraded heavily on sorted input (close to O(n^2)).
   - Insertion and Bubble Sort matched expected O(n^2) patterns; practical only for small n.
   - Selection Sort was consistently slower than Insertion.

3. **Binary Search**

   - Observed near-constant execution time, aligning with O(log n).
   - Memory usage negligible.

4. **Memory Observations**
   - Recursive Fibonacci showed stack usage spikes.
   - Merge Sort consumed extra memory due to merging process.
   - Others were memory-light as expected.

**Conclusion**: Observations strongly matched theoretical complexities.  
Efficient algorithms (Merge Sort, Quick Sort, Binary Search, DP Fibonacci) are practically viable, while Bubble, Selection, and Recursive Fibonacci are mostly educational.
