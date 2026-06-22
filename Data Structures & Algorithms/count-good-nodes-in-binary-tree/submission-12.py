# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_nodes = 0

        if root:
            stk = [(root, root.val, float("-inf"))]

        while stk:

            node, val, max_seen = stk.pop()

            if max_seen <= val:
                good_nodes += 1
            
            max_seen = max(max_seen, val)

            if node.right: stk.append((node.right, node.right.val, max_seen))
            if node.left: stk.append((node.left, node.left.val, max_seen))

        return good_nodes