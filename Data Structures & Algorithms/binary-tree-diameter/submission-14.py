"""
 0        1 3
    0             +1 2 3
            +23         4 + 1
    
    +1 5

0       0

max(left_h, right_h) + 1

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_height = [0]

        def dfs(node):

            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            max_height[0] = max(max_height[0], left_height + right_height)

            return max(left_height, right_height) + 1

        dfs(root)

        return max_height[0]

"""
[3]




"""