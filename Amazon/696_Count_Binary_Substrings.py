class Solution(object):
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)

# Complexity Analysis

# Time Complexity: O(N), where N is the length of s. Every loop is through O(N) items with O(1) work inside the for-block.

# Space Complexity: O(1), the space used by prev, cur, and ans.