"""
Binary Search Implementation
----------------------------
Requires sorted input array.
"""

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search(arr, target)
    print("Binary Search Result: Index =", result)
