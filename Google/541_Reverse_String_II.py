class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in xrange(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)

# Complexity Analysis

# Time Complexity: O(N), where N is the size of s. We build a helper array, plus reverse about half the characters in s.

# Space Complexity: O(N), the size of a.