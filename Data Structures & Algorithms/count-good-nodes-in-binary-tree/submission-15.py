# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        """ 
                          3
                        3   1
                       3   1 5

        good_nodes = 1

        stk = []
        (node,maxx)
        node.val > maxx:

        if node.left: stk.append(node.left)
        """
        good_nodes = 0
        stk = [(root, float("-inf"))]

        while stk:

            node, maxx = stk.pop()

            if node.val >= maxx:
                good_nodes += 1
                maxx = max(maxx, node.val)

            if node.left: stk.append((node.left, maxx))
            if node.right: stk.append((node.right, maxx))

        return good_nodes