# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        stk = [(root, 1)]
        max_depth = 0

        while stk:
            node, depth = stk.pop()
            max_depth = max(depth, max_depth)
            if node.right: stk.append((node.right, depth + 1))
            if node.left: stk.append((node.left, depth + 1))
        
        return max_depth
