# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, maxx, minn):

            if not node:
                return True

            if not minn < node.val < maxx:
                return False
            
            if dfs(node.left, node.val, minn) and dfs(node.right, maxx, node.val):
                return True
            
            else:
                return False
        
        return dfs(root, float("inf"), float("-inf"))
