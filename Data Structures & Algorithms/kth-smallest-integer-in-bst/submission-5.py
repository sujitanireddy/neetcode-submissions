"""
inorder: left -> node -> right

res = []
do inorder traveral and get the values out

iterate k times and return the value
       i
 0 1 2 3
[2 3 4 5]

k = 4

TC: O(n)
SC: O(n)

[0]

[0]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = []

        def dfs(node):

            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        return res[k-1]



