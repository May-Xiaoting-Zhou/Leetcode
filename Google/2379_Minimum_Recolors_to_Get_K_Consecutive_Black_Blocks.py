class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        num_whites = 0
        num_recolors = float("inf")

        # Move right pointer
        for right in range(len(blocks)):

            # Increment num_whites if block at right pointer is white
            if blocks[right] == "W":
                num_whites += 1

            # k consecutive elements are found
            if right - left + 1 == k:

                # Update minimum
                num_recolors = min(num_recolors, num_whites)

                # Decrement num_whites if block at left pointer is white
                if blocks[left] == "W":
                    num_whites -= 1

                # Move left pointer
                left += 1

        return num_recolors

# Complexity Analysis
# Let N be the size of blocks.

# Time Complexity: O(N)

# The algorithm iterates through each element of blocks exactly once, performing constant-time operations on each element. Specificially, in each iteration, it performs arithmetic operations, whose time complexities are independent of the input size. Therefore, the overall time complexity is linear to the number of elements in blocks, O(n).

# Space Complexity: O(1)

# The space required does not depend on the size of the input value or any data structures that require additional space, so only constant O(1) space is used.