class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = [nums]
        # total = 1
        # for i in range(1, len(nums) + 1):
        #     total *= i

        # while len(res) < total:
        #     for lst in res:
        #         for i in range(1, len(lst)):
        #             temp = lst.copy()
        #             temp[0], temp[i] = temp[i], temp[0]
        #             if temp not in res:
        #                 res.append(temp)
        
        # return res
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    backtrack(curr)
                    curr.pop()
        ans = []
        backtrack([])
        return ans

# Complexity Analysis
# Time complexity : O(n⋅n!). 
# Space complexity : O(n).