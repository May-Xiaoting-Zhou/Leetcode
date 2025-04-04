class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        carry = 0
        idx_1, idx_2 = len(num1) - 1, len(num2) - 1
        res = ""
        while idx_1 >= 0 or idx_2 >= 0:
            x1 = ord(num1[idx_1]) - ord("0") if idx_1 >=0 else 0
            x2 = ord(num2[idx_2]) - ord("0") if idx_2 >=0 else 0

            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res = str(value) + res

            idx_1 -= 1
            idx_2 -= 1

        if carry:
            res = str(carry) + res
        return res

# Complexity Analysis

# Time Complexity: O(max(N 1 ,N 2)), where N 1 and N 2  are length of nums1 and nums2. Here we do max(N 1,N 2) iterations at most.

# Space Complexity: O(max(N 1,N 2)), because the length of the new string is at most max(N 1 ,N 2)+1.