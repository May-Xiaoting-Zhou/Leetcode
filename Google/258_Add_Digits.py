class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0

# Complexity Analysis
# Let n be the input number.

# Time complexity: O(1)

# The function performs a constant number of operations, regardless of the input size. The operations involve simple arithmetic calculations and a conditional check, all of which take constant time.

# Space complexity: O(1)

# The function uses a constant amount of extra space. It does not depend on the input size and only uses a few variables for the calculations, which do not grow with the input.