class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Dictionary to store frequency of occurrence of each character
        frequency_map = {}
        # Count frequencies
        for c in s:
            frequency_map[c] = frequency_map.get(c, 0) + 1

        res = 0
        has_odd_frequency = False
        for freq in frequency_map.values():
            # Check if the frequency is even
            if (freq % 2) == 0:
                res += freq
            else:
                # If the frequency is odd, one occurrence of the
                # character will remain without a match
                res += freq - 1
                has_odd_frequency = True

        # If has_odd_frequency is true, we have at least one unmatched
        # character to make the center of an odd length palindrome.
        if has_odd_frequency:
            return res + 1

        return res

# Complexity Analysis
# Let n be the length of the given string s.

# Time complexity: O(n)

# The algorithm goes through the characters of s twice: once to count their frequencies and once to construct the palindrome. Since hash table operations like inserting and updating take constant time (O(1)), the time complexity of the algorithm is O(2⋅n), which simplifies to O(n).

# Space complexity: O(1)

# The algorithm uses a hash table to store the frequency of characters. Given that there can be at most 52 unique characters in s, the space complexity is O(52), which can be simplified to O(1) space.