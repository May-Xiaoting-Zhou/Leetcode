class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n

# Complexity Analysis

# Time complexity: O(1).

# Space complexity: O(1).