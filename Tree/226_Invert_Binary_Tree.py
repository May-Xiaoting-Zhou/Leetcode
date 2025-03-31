# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # Deque
        # dq = collections.deque([root])
        # while dq:
        #     pop_nodes = dq.popleft()
        #     if pop_nodes:
        #         pop_nodes.left, pop_nodes.right = pop_nodes.right, pop_nodes.left
        #         dq.append(pop_nodes.left)
        #         dq.append(pop_nodes.right)
        # return root
        # Recursive
        if root:
            lt = self.invertTree(root.left)
            rt = self.invertTree(root.right)
            root.left, root.right = rt, lt
            return root

# Complexity Analysis
# Time complexity : O(n). 
# Space complexity : The Worst case O(n), normally O(log(N))