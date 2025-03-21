class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

# Complexity Analysis

# Time complexity : O(n)

# Because the set allows for O(1) containment queries, the main loop
# runs in O(n) time. Creating num_set costs O(n) time, as each set insertion
# runs in amortized O(1) time, so the overall runtime is O(n+n)=O(n).

# Space complexity : O(n)

# nums contains n−1 distinct elements, so it costs O(n) space to
# store a set containing all of them.