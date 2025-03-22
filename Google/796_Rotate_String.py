class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Check if the lengths are different
        if len(s) != len(goal):
            return False

        # Create a new string by concatenating 's' with itself
        doubled_string = s + s

        # Use find to search for 'goal' in 'doubledString'
        # If find returns an index that is not -1
        # then 'goal' is a substring
        return doubled_string.find(goal) != -1

# Complexity Analysis
# Let n be the size of string s (and also the size of string goal, since they must be of equal length to be rotations).

# Time complexity: O(n)

# Checking if the lengths of both strings are different takes O(n).

# Concatenating the string s with itself to create doubledString takes O(n) because we are creating a new string that is twice the length of s.

# The substring find function is typically implemented using an algorithm that runs in O(n). This involves scanning the doubledString of length 2n for the substring goal of length n. Since the search occurs in a string of size 2n, the overall complexity for this operation remains O(n).

# Overall, the most significant operations are linear in terms of n, resulting in a total time complexity of O(n).

# Space complexity: O(n)

# The space used for the doubledString is O(n) since it stores a string that is double the size of s (specifically, O(2⋅n)≈O(n)).

# Thus, the overall space complexity is O(n) due to the concatenated string.