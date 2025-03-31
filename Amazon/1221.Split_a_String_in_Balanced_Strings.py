class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = {'L': 0, 'R': 0}
        res = 0
        i = 0
        while i < len(s):
            while cnt['L'] == 0 or cnt['L'] != cnt['R']:
                cnt[s[i]] += 1
                i += 1
            res += 1
            cnt = {'L': 0, 'R': 0}
        return res

# Complexity Analysis

# Time complexity : O(n). 

# Space complexity : O(1). 