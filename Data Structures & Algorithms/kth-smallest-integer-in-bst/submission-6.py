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

[2]
    
          

res = []

     


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
        stk = []
        curr = root

        while stk or curr:

            while curr:
                stk.append(curr)
                curr = curr.left
            
            node = stk.pop()
            res.append(node.val)

            if node.right:
                curr = node.right
        
        return res[k-1]






