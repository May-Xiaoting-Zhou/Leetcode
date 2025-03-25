class Solution(object):
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]

# Complexity Analysis

# Time complexity : O(log n/2)=O(logn). Same as the binary search above, except we are only binary searching half the elements, rather than all of them.

# Space complexity : O(1). Same as the other approaches. We are only using constant space to keep track of where we are in the search.