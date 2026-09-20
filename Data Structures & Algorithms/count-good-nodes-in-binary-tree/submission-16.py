"""
the root of the tree is a good node always

                    2
                
            1
        
        3

    2

We keep track of maximum while we go down and validate if it's a good node!

[(]




good_nodes = 2
maxx = 2



O(n)
O(h)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good_nodes = 0
        stk = [(root, float("-inf"))]       #tuple (curr_val, max)

        while stk:
            node, maxx = stk.pop()

            if node.val >= maxx:
                good_nodes += 1
                maxx = node.val
            
            if node.right: stk.append((node.right, maxx))
            if node.left: stk.append((node.left, maxx))

        return good_nodes

"""

                3
            
        3               N

4             2




"""

    



        