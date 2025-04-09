class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # cnt = Counter(nums)
        # res = []
        # for i in range(1, len(nums) + 1):
        #     if not cnt[i]:
        #         res.append(i)
        # return res

        cnt = {i: 1 for i in range(1, len(nums) + 1)}
        for n in set(nums):
            del cnt[n]
        return list(cnt.keys())

        # s = set([i for i in range(1, len(nums) + 1)])
        # res = s - set(nums)
        # return list(res)       

# Complexity Analysis

# Time Complexity : O(N)
# Space Complexity : O(N)