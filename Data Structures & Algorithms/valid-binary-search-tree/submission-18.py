"""
           6
        4     8
     2    5 


(minn, 4)
(4, maxx)

update max while going to left subtree
update the min while going to right subtree

DFS - iterativley
TC : O(n)
SC : O(h)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        """
        [(3,2,inf)  ]


        """
        
        stk = [(root, float("-inf"),float("inf"))] #node, minn, maxx

        while stk:

            node, minn, maxx = stk.pop()

            if not minn < node.val < maxx:
                return False
            
            if node.right: stk.append((node.right, node.val, maxx))
            if node.left: stk.append((node.left, minn, node.val))
        
        return True





















