# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        largest_diameter = 0

        def length(root):

            nonlocal largest_diameter

            if not root:
                return 0
            
            left_height = length(root.left)
            right_height = length(root.right)

            diameter = left_height + right_height

            largest_diameter = max(largest_diameter, diameter)

            return 1 + max(left_height, right_height)   

        length(root)

        return largest_diameter  