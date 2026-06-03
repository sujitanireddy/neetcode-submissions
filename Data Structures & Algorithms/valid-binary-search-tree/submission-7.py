# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(node, minn, maxx):

            if not node:
                return True

            if not (minn < node.val < maxx):
                return False
            
            return is_valid(node.right, node.val, maxx) and is_valid(node.left, minn, node.val)
        
        return is_valid(root, float("-inf"), float("inf"))