class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        write_index = 0  # Pointer to place non-zero elements

        for index in range(n):
            # Step 1: Merge adjacent equal elements if they are non-zero
            if (
                index < n - 1
                and nums[index] == nums[index + 1]
                and nums[index] != 0
            ):
                nums[index] *= 2
                nums[index + 1] = 0
            # Step 2: Shift non-zero elements to the front
            if nums[index] != 0:
                if index != write_index:
                    nums[index], nums[write_index] = (
                        nums[write_index],
                        nums[index],
                    )
                write_index += 1
        return nums

# Complexity Analysis
# Let n be the size of the nums array.

# Time Complexity: O(n)

# We iterate through the array only once, performing constant-time operations for each element. The merging operation modifies elements in-place, and the shifting of non-zero values is handled dynamically as we iterate, ensuring that no additional passes are required. Since every operation is handled in a single pass, the overall complexity remains linear.

# Space Complexity: O(1)

# The algorithm modifies the input array in place without using extra space. Only a few integer variables are used, which take constant space. Therefore, the overall space complexity is O(1).