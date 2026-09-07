"""
base case
- if not node:
    return 0

core algo:
left_max = dfs(root.left)
right_max = dfs(root.right)

left_max = max(left_max, 0)
right_max = max(right_max, 0)

capture the best in a global variable

return max(left_max, right_max)

Only promote the sum of one branch: choose the max sum
if negative number: promote zero

TC: O(n)
SC: O(h)


                                        -15

                                10              20
                            
                            
                                        15              5

                                    -5

           0 
max_sum = [40]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = [root.val]

        def dfs(node):

            #base case
            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            max_sum[0] = max(node.val + left_max + right_max, max_sum[0])

            return node.val + max(left_max, right_max)

        dfs(root)

        return max_sum[0]

























