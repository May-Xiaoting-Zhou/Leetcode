# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is not None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

# Complexity Analysis

# Time complexity: O(n)

# The time complexity is O(n) because the recursive function is T(n)=2⋅T(n/2)+1.
# Space complexity: O(n)

# The worst case space required is O(n), and in the average case it's O(logn) where n is number of nodes.