# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = 0
        
        def height(root):

            nonlocal max_diameter

            if not root:
                return 0

            right_height = height(root.right)
            left_height = height(root.left)

            diameter = right_height + left_height

            max_diameter = max(max_diameter, diameter)

            return 1 + max(right_height, left_height)
        
        height(root)

        return max_diameter