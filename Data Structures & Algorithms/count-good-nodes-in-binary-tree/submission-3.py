# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0
        
        stk = [(root, float("-inf"))]

        while stk:

            node, maxx = stk.pop()

            if node.val >= maxx:
                maxx = node.val
                good_nodes += 1

            if node.right:
                stk.append((node.right, maxx))
            
            if node.left:
                stk.append((node.left, maxx))
        
        return good_nodes