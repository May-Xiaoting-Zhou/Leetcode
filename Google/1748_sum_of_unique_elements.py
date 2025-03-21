class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum_unique = 0
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        for i in range(len(nums)):
            if i == 0 and i + 1 < len(nums) and nums[i] != nums[i + 1]:
                sum_unique += nums[i]
            
            if i - 1 >= 0 and i == len(nums) - 1 and nums[i] != nums[i - 1]: 
                sum_unique += nums[i]
            
            if i > 0 and i + 1 < len(nums) and (nums[i] != nums[i - 1] and nums[i] != nums[i + 1]):
                sum_unique += nums[i]
        return sum_unique
                
# Complexity Analysis

# Time complexity : O(n).

# Space complexity : O(1). No additional space is used.