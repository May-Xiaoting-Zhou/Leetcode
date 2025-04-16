class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]

        # if len(nums) >= 2:
        #     pre_pre = nums[0]
        #     pre = max(nums[1], pre_pre)
        #     curr = pre

        #     for i in range(2, len(nums)):
        #         curr = max(pre_pre + nums[i], pre)
        #         pre_pre = pre
        #         pre = curr
                
        #     return curr

        self.memo = {}

        return self.robFrom(0, nums)

    def robFrom(self, idx: int, nums: list) -> int:
        if idx >= len(nums):
            return 0
        
        if idx in self.memo:
            return self.memo[idx]
        
        self.memo[idx] = max(self.robFrom(idx + 1, nums), self.robFrom(idx + 2, nums) + nums[idx])

        return self.memo[idx]         

# Approach 1: Recursion with Memoization
# Complexity Analysis

# Time Complexity: O(N) since we process at most N recursive calls, thanks to caching, and during each of these calls, we make an O(1) computation which is simply making two other recursive calls, finding their maximum, and populating the cache based on that.

# Space Complexity: O(N) which is occupied by the cache and also by the recursion stack.

# Approach 2: Dynamic Programming
# maxRobbedAmount[i] = max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + nums[i])
# Time Complexity

# Time Complexity: O(N) since we have a loop from N−2⋯0 and we use the precalculated values of our dynamic programming table to calculate the current value in the table which is a constant time operation.

# Space Complexity: O(1/N) since we are not using a table to store our values. Simply using two variables will suffice for our calculations.
