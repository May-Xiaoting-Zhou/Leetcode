class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

# Complexity Analysis
# Time complexity: O(n+m), where n and m are the arrays' lengths in the average case and O(n×m) in the worst case when the load factor is high enough.

# Space complexity: O(m+n) because in the worst case, when all elements in the arrays are unique, n space is used to store set1 and m space is used to store set2. The space used to store the result is not counted in the space complexity.