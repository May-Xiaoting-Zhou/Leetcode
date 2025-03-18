class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)): # O(n), O(n) -> O(1)
            nums[i] += nums[i - 1]
        return nums

# Complexity Analysis
# Time complexity: O(n) where n is the length of input array.

# Space complexity: O(1) since we don't use any additional space to find the running sum. Note that we do not take into consideration the space occupied by the output array.