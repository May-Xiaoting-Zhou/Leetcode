# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # # Stack FILO
        # if not root:
        #     return 0
        # stack = [(root, 1)]
        # min_depth = float('inf')
        # while stack:
        #     pop_node, depth = stack.pop()
        #     if not pop_node.left and not pop_node.right:
        #         min_depth = min(depth, min_depth)
        #     if pop_node.left:
        #         stack.append((pop_node.left, depth + 1))
        #     if pop_node.right:
        #         stack.append((pop_node.right, depth + 1))
        # return min_depth
        # # BFS
        # def BFS(stack) -> int:
        #     new_stack = []
        #     while stack:
        #         node, level = stack.pop()
        #         if not node.left and not node.right:
        #             return level

        #         if node.left:
        #             new_stack.append((node.left, level + 1))
        #         if node.right:
        #             new_stack.append((node.right, level + 1))
            
        #     return BFS(new_stack)
        
        # if not root:
        #     return 0
        # else:
        #     return BFS([(root, 1)])
        # # DFS
        # if not root:
        #     return 0
        # else:
        #     lt = self.minDepth(root.left) + 1
        #     rt = self.minDepth(root.right) + 1

        #     if lt == 1:
        #         return rt
        #     if rt == 1:
        #         return lt
            
        #     return min(lt, rt)
        # Deque
        if not root:
            return 0
        
        dq = collections.deque([root])
        dpth = 0
        
        while dq:
            dpth += 1
            dq_size = len(dq)
            for _ in range(dq_size):
                p = dq.popleft()
                if not p.left and not p.right:
                    return dpth
                if p.left:
                    dq.append(p.left)
                if p.right:
                    dq.append(p.right)
        return dpth


# Complexity Analysis
# Time complexity : O(n). 
# Space complexity : The Worst case O(n), normally O(log(N))