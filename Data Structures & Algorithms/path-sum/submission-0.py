# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        self.vals = []

        def findsum(root):

            if not root:
                return False
            
            self.vals.append(root.val)

            if not root.left and not root.right and sum(self.vals) == targetSum:
                return True
            
            if findsum(root.left):
                return True
            
            if findsum(root.right):
                return True
            
            self.vals.pop()

            return False
        
        return findsum(root)

        