# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Approach 2: Iteration
        # node = root
        # while node:
        #     if val < node.val:
        #         if not node.left:
        #             node.left = TreeNode(val)
        #             return root
        #         else:
        #             node = node.left
        #     else:
        #         if not node.right:
        #             node.right = TreeNode(val)
        #             return root
        #         else:
        #             node = node.right
        # return TreeNode(val)
        # Approach 1: Recursion
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

# Complexity Analysis

# Time complexity : O(H), where H is a tree height.

# Approach 1: Recursion
# Space complexity : O(H) to keep the recursion stack, i.e. O(logN) in the average case, and O(N) in the worst case.
# Approach 2: Iteration
# Space complexity : O(1) since it's a constant space solution.