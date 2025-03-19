class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        freq = {}

        # Store frequency of each number in the grid
        for row in grid:
            for num in row:
                freq[num] = freq.get(num, 0) + 1

        # Check numbers from 1 to n^2 to find missing and repeated values
        for num in range(1, n * n + 1):
            if num not in freq:
                missing = num  # Number not present in grid
            elif freq[num] == 2:
                repeat = num  # Number appears twice

        return [repeat, missing]

# Complexity Analysis

# Let n be the side length of the grid.

# Time complexity: O(n ** 2)

# The algorithm makes two main passes. First, we iterate through each cell in our n×n grid to build the frequency map, which takes O(n ** 2) operations. 
# Then, we iterate through numbers from 1 to n ** 2 to find our missing and repeated values, which takes O(n ** 2) operations. 

# Since both passes are sequential and take O(n ** 2) time, our overall time complexity is O(n ** 2).

# Space complexity: O(n ** 2)

# The algorithm uses a hash map to store the frequency of each number. The map will store all unique numbers from 1 to n ** 2 except the missing number, making the space complexity O(n ** 2).