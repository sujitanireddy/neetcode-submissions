# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [float("-inf")]
        
        def dfs(node):
            
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            left_height = max(left_height, 0)
            right_height = max(right_height, 0)

            res[0] = max(res[0], node.val + left_height + right_height)

            return max(node.val + left_height, node.val + right_height)           

        dfs(root)

        return res[0]