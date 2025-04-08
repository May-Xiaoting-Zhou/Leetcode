class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        subSum = 0
        dic = collections.defaultdict(int)
        dic[0] = 1
        for i in range(len(nums)):
            subSum += nums[i]
            if subSum - k in dic:
                cnt +=  dic[subSum - k]

            dic[subSum] += 1
        return cnt
        # cnt = 0
        # for i in range(len(nums)):
        #     subSum = 0
        #     for j in range(i, len(nums)):
        #         subSum += nums[j]
        #         if subSum == k:
        #             cnt += 1
        # return cnt

# Complexity Analysis

# Time complexity : O(n). The entire nums array is traversed only once.

# Space complexity : O(n). Hashmap map can contain up to n distinct entries in the worst case.