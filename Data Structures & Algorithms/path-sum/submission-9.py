# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        """
        
        Basecases
        - if not root return: False
        - if we hit the root and the targetsum != summ: return False
        - if we hit the root and the targetsum == summ: return True

        """

        def dfs(root, summ):

            if not root:
                return False
                
            summ += root.val

            if not root.left and not root.right and summ == targetSum:
                return True
            
            if dfs(root.left, summ):
                return True 
            
            if dfs(root.right, summ):
                return True
            
            return False

        return dfs(root, 0)