class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_0, idx_2 = 0, len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i > idx_0:
                nums[i], nums[idx_0] = nums[idx_0], nums[i]
                idx_0 += 1
                i -= 1
            
            if nums[i] == 2 and i < idx_2:
                nums[i], nums[idx_2] = nums[idx_2], nums[i]
                idx_2 -= 1
                i -= 1

            i += 1

# Complexity Analysis

# Time complexity : O(N) since it's one pass along the array of length N.

# Space complexity : O(1) since it's a constant space solution