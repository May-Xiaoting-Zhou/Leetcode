class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA

            maxLeftA = (
                float("-inf") if partitionA == 0 else nums1[partitionA - 1]
            )
            minRightA = float("inf") if partitionA == m else nums1[partitionA]
            maxLeftB = (
                float("-inf") if partitionB == 0 else nums2[partitionB - 1]
            )
            minRightB = float("inf") if partitionB == n else nums2[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (
                        max(maxLeftA, maxLeftB) + min(minRightA, minRightB)
                    ) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partitionA - 1
            else:
                left = partitionA + 1

# Complexity Analysis
# Let m be the size of array nums1 and n be the size of array nums2.

# Time complexity: O(log(min(m,n)))

# We perform a binary search over the smaller array of size min(m,n).
# Space complexity: O(1)

# The algorithm only requires a constant amount of additional space to store and update a few parameters during the binary search.