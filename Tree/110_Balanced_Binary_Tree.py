# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # self.res = True
        # def check(node) -> int:
        #     if not node:
        #         return 0
        #     else:
        #         height_lt = check(node.left)
        #         height_rt = check(node.right)
        #         if abs(height_lt - height_rt) > 1:
        #             self.res = False
        #         return max(height_lt, height_rt) + 1
        
        # check(root)
        # return self.res
        return self.isBalancedHelper(root)[0]
    def isBalancedHelper(self, root: TreeNode) -> (bool, int):
        if not root:
            return True, -1
        leftIsBalanced, ltHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rtHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0
        return (abs(ltHeight - rtHeight) < 2, (1 + max(ltHeight, rtHeight)))

# Complexity Analysis
# Time complexity : O(n). 
# Space complexity : The Worst case O(n).