class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # Initialize ch with 0, because 0 ^ X = X
        # 0 when XORed with any bit would not change the bits value.
        ch = 0

        # XOR all the characters of both s and t.
        for char_ in s:
            ch ^= ord(char_)

        for char_ in t:
            ch ^= ord(char_)

        # What is left after XORing everything is the difference.
        return chr(ch)

# Complexity Analysis

# Time Complexity: O(N), where N is length of the strings. Since, we iterate through both the strings once.

# Space Complexity: O(1). The problem states string s and string t have lowercase letters. Thus, the total number of unique characters and eventually buckets in the hash map possible are just 26.