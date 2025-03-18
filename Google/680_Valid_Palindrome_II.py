class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True

# Complexity Analysis

# Given N as the length of s,

# Time complexity: O(N).

# The main while loop we use can iterate up to N / 2 times, since each iteration represents a pair of characters. On any given iteration, we may find a mismatch and call checkPalindrome twice. checkPalindrome can also iterate up to N / 2 times, in the worst case where the first and last character of s do not match.

# Because we are only allowed up to one deletion, the algorithm only considers one mismatch. This means that checkPalindrome will never be called more than twice.

# As such, we have a time complexity of O(N).

# Space complexity: O(1).

# The only extra space used is by the two pointers i and j, which can be considered constant relative to the input size.