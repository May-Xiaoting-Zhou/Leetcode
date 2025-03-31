class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "N"
            return f"({node.val}, {serialize(node.left)}, {serialize(node.right)})"
        rootSerialized = serialize(root)
        subRootSerialized = serialize(subRoot)
        return subRootSerialized in rootSerialized

# Complexity Analysis
# Time complexity : O(n+m). 
# Space complexity : The Worst case O(n +m ).