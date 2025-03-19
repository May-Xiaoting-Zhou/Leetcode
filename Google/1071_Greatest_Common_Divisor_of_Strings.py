
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        
        def valid(k):
            if len1 % k or len2 % k: 
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base 
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""

# Complexity Analysis
# Let m,n be the lengths of the two input strings str1 and str2.

# Time complexity: O(min(m,n)⋅(m+n))
# We checked every prefix string base of the shorter string among str1 and str2, and verify if both strings are made by multiples of base. There are up to min(m,n) prefix strings to verify and each check involves iterating over the two input strings to check if the current base is the GCD string, which costs O(m+n). Therefore, the overall time complexity is O(min(m,n)⋅(m+n)).

# Space complexity: O(min(m,n))
# We need to keep a copy of base in each iteration, which takes O(min(m,n)) space.