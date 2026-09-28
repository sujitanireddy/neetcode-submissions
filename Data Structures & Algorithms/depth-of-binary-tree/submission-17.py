"""
early return case:
if not root:
    return 0

            1 +1        (1) max(left, right) 
        
       1 2      1 3



            4 + 1

TC : O(n)
SC : O(h)

"""
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
        
        def dfs(node):
            
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            return max(left_height, right_height) + 1

        return dfs(root)