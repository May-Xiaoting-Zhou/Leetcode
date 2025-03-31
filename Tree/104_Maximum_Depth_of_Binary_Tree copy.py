# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # Method 1: DFS
        # if not root:
        #     return 0
        # else:
        #     lt_depth = self.maxDepth(root.left) + 1
        #     rt_depth = self.maxDepth(root.right) + 1
        #     return max(lt_depth, rt_depth)

        # # Method 2: BFS
        # def BFSTraversal(stack) -> int:
        #     if len(stack) == 0:
        #         return self.Maxheight
        #     else:
        #         new_stack = []
        #         while stack:
        #             pop_node, level = stack.pop()
        #             self.Maxheight = level + 1
        #             if pop_node.left:
        #                 new_stack.append((pop_node.left, level + 1))
        #             if pop_node.right:
        #                 new_stack.append((pop_node.right, level + 1))

        #     return BFSTraversal(new_stack)
        
        # if root:
        #     stack = [(root, 0)]
        #     self.Maxheight = 0
        #     return BFSTraversal(stack)
        # else:
        #     return 0

        # Method 3: Stack FILO
        max_depth = 0
        stack = []
        if root:
            curr_depth = 1
            stack = [(1, root)]
        
        while stack:
            curr_depth, pop_node = stack.pop()
            max_depth = max(max_depth, curr_depth)
            if pop_node.left:
                stack.append((curr_depth + 1, pop_node.left))

            if pop_node.right:
                stack.append((curr_depth + 1, pop_node.right))
        return max_depth


# Complexity Analysis
# Time complexity : O(n). 
# Space complexity : The Worst case O(n), normally O(log(N))