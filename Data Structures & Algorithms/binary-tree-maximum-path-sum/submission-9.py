# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        #at every node let's calculate two things
            #leftsubtree summation, rightsubtree summation
            #total inculding the root
        #if -ve value is being returend, convert it to zero (we don't want to accout for -ve values)

        maxsum = [root.val]

        def dfs(root):

            if not root:
                return 0 
            
            max_left = dfs(root.left)
            max_right = dfs(root.right)

            max_left = max(0, max_left)
            max_right = max(0, max_right)

            maxsum[0] = max(maxsum[0], (max_left + max_right + root.val))

            return root.val + max(max_left, max_right)
        
        dfs(root)

        return maxsum[0]

