# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        DIAMETER = [float("-inf")]

        def dfs(root):
            
            if not root:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            DIAMETER[0] = max(DIAMETER[0], left_height + right_height)

            return max(left_height, right_height) + 1

        dfs(root)
        return DIAMETER[0]