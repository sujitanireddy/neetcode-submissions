# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        currsum = [0]

        def dfs_sum(root):

            if not root:
                return False
            
            currsum[0] += root.val

            if (not root.left and not root.right) and currsum[0] == targetSum:
                return True

            if (not root.left and not root.right) and currsum[0] != targetSum:
                currsum[0] -= root.val
                return False
            
            if dfs_sum(root.left):
                return True
            
            if dfs_sum(root.right):
                return True
            
            currsum[0] -= root.val

            return False

        return dfs_sum(root)

            

            

            

    