# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        stk = []
        
        if root:
            stk.append((root, float("-inf")))

        good_nodes = 0

        while stk:

            node, max_seen = stk.pop()

            if  node.val >= max_seen:
                good_nodes += 1

            max_seen = max(max_seen, node.val)

            if node.right: stk.append((node.right, max_seen))
            if node.left: stk.append((node.left, max_seen))
        
        return good_nodes
