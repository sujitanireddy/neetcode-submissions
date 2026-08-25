"""
              -15 (0)
               
               
        10 (-10)      20 (20)

                     15 (35)   5 (15)

                    -5 (30)
                    

if not root:
    return 0

if (root.val + prevSum) == targetSum:
    return True

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root,prevSum):

            if not root:
                return False
            
            if not root.left and not root.right and root.val + prevSum == targetSum:
                return True
            
            return dfs(root.left, root.val + prevSum) or dfs(root.right, root.val + prevSum)
        
        return dfs(root, 0)