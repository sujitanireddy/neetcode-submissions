# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0
        stk = []

        if root:
            stk.append((root, float("-inf")))
        
        while stk:

            node, val = stk.pop()

            if node.val >= val:
                good_nodes += 1

            val = max(val, node.val)

            if node.right: stk.append((node.right, val))
            if node.left: stk.append((node.left, val))
        
        return good_nodes

