# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isbalanced = True
        
        def height(root):

            nonlocal isbalanced

            if not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                isbalanced = False
            
            return 1 + max(left_height, right_height)
        
        height(root)

        return isbalanced


        