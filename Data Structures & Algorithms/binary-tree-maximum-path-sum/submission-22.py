# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        MAX_PATH_SUM = [float("-inf")]
        
        def dfs(root):
            
            if not root:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            left_height = max(left_height, 0)
            right_height = max(right_height, 0)

            MAX_PATH_SUM[0] = max(MAX_PATH_SUM[0], left_height + right_height + root.val)

            return max(left_height, right_height) + root.val
        
        dfs(root)
        return MAX_PATH_SUM[0]