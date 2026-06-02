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
            
            left_h = height(root.left)
            right_h = height(root.right)

            if abs(left_h - right_h) > 1:
                isbalanced = False
            
            return max(left_h, right_h) + 1
        
        height(root)

        return isbalanced