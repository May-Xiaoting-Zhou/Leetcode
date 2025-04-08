class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if not nums:
                return res
            
            avg_v = target // k
            if avg_v < nums[0] or nums[-1] < avg_v:
                return res
            
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1 :], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res
        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            s = set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                    s.add(nums[i])
            return res
        # def twoSum(nums: List[int], target: int) -> List[List[int]]:
        #     res = []
        #     lo, hi = 0, len(nums) - 1
        #     while lo < hi:
        #         curr_sum = nums[lo] + nums[hi]
        #         if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]) :
        #             lo += 1
        #         elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
        #             hi -= 1
        #         else:
        #             res.append([nums[lo], nums[hi]])
        #             lo += 1
        #             hi -= 1
        #     return res
        nums.sort()
        return kSum(nums, target, 4)

# Complexity Analysis

# Time Complexity: O(n ** k−1), or O(n ** 3) for 4Sum. We have k−2 loops, and twoSum is O(n).

# Note that for k>2, sorting the array does not change the overall time complexity.

# Space Complexity: O(n). We need O(k) space for the recursion. k can be the same as n in the worst case for the generalized algorithm.

# Note that, for the purpose of complexity analysis, we ignore the memory required for the output.