# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # def inorderTraversalNodes(root, lst) -> List[int]:
        #     if not root:
        #         return lst
        #     else:
        #         inorderTraversalNodes(root.left, lst)
        #         lst.append(root.val)
        #         inorderTraversalNodes(root.right, lst)
        #     return lst

        # return inorderTraversalNodes(root, [])
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right 
        return res
        

# Complexity Analysis
# Time complexity : O(n). 
# Space complexity : The Worst case O(n), normally O(log(N))