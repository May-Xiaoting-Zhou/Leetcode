class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff

# Complexity Analysis

# Time Complexity: O(n ** 2). We have outer and inner loops, each going through n elements.

# Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n ** 2). This is asymptotically equivalent to O(n ** 2).

# Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm.