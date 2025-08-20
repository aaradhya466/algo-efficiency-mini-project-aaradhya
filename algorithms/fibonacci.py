"""
Fibonacci Algorithm Implementations
-----------------------------------

1. Naïve Recursive
2. Dynamic Programming (Memoization)
"""

# 1. Naïve Recursive Fibonacci
def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


# 2. Dynamic Programming (Memoization)
def fib_dp(n: int, memo=None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]


# Example usage
if __name__ == "__main__":
    n = 10
    print("Naïve Recursive Fibonacci:", fib_recursive(n))
    print("DP Fibonacci:", fib_dp(n))
