class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        cnt = 0
        for ch in s:
            if ch == '(':
                if cnt:
                    ans += ch
                cnt += 1
            else:
                cnt -= 1
                if cnt:
                    ans += ch
        return ans

# Complexity Analysis

# Time complexity : O(n).

# Space complexity : O(1). 