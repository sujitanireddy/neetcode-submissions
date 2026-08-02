# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        stk = [(root,min,max)]

        """

        stk = [(root,float("inf"),float("-inf"))] #(root.val, max, min)

        while stk:

            node, maxx, minn = stk.pop()

            if not minn < node.val < maxx:
                return False 

            if node.left: stk.append((node.left, node.val, minn))
            if node.right: stk.append((node.right,maxx,node.val))
        
        return True