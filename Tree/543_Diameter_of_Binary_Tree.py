# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def getLongestPath(node, path) -> int:
            if not node:
                return 0
            else:
                lt_path = getLongestPath(node.left, path)
                rt_path = getLongestPath(node.right, path)
                self.diameter = max(self.diameter, lt_path + rt_path)
                return max(lt_path, rt_path) + 1

        getLongestPath(root, 0)
        return self.diameter

# Complexity Analysis
# Time complexity : O(n). 
# Space complexity : The Worst case O(n).