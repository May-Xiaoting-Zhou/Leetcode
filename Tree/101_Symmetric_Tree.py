# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: 
        # # Recursive
        # def mirror(root1, root2) -> bool:
        #     if not root1 and not root2:
        #         return True
        #     if not root1 or not root2:
        #         return False
            
        #     if root1.val != root2.val:
        #         return False
        #     return (mirror(root1.left, root2.right) and mirror(root1.right, root2.left))
        
        # return mirror(root.left, root.right)
        # Iterative
        q = [root, root]
        while q:
            root1, root2 = q.pop(0), q.pop(0)
            if not root1 and not root2:
                continue
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            q.append(root1.left)
            q.append(root2.right)
            q.append(root1.right)
            q.append(root2.left)
        return True


# Complexity Analysis
# Time complexity : O(n). 
# Space complexity : The Worst case O(n).