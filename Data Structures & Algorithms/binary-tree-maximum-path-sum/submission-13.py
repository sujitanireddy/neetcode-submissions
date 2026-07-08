# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        """ 

        #base case
        if not root:
            return 0

        - go find the maximum sum from left subtree
        - go find the maximum sum from right subtree
        - find the maximum sum inculding the node
        - Keep track of the maximum
        
        """

        max_sum_so_far = [float("-inf")]

        def dfs(root):

            if not root:
                return 0
            
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            left_max = max(left_max, 0)
   
            right_max = max(right_max, 0)
   

            max_sum_so_far[0] = max(max_sum_so_far[0], left_max + right_max + root.val)


            return max(left_max, right_max) + root.val

        dfs(root)

        return max_sum_so_far[0]


