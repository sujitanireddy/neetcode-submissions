# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], minn = float("-inf"), maxx = float("inf")) -> bool:

        if not root:
            return True

        if not (minn < root.val < maxx):
            return False
            
        return self.isValidBST(root.right, root.val, maxx) and self.isValidBST(root.left, minn, root.val)