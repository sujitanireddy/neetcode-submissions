"""
- max_so_far

stk = [(root,float("-inf"))] #node, max

while stk:

    node, maxx = stk.pop()

    maxx = max(maxx, node.val)

    if node.left: stk.append(node.left, maxx)
    if nod.right: stk.append(node.right, maxx)


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.pathsum = float("-inf")

        def dfs(root):

            if not root:
                return 0
            
            left_max = dfs(root.left)
            right_max = dfs(root.right)

            self.pathsum = max(self.pathsum, root.val + left_max + right_max)

            if root.val + left_max + right_max < 0:
                 return 0

            return max(left_max, right_max) + root.val
        
        dfs(root)

        return self.pathsum


            

            

