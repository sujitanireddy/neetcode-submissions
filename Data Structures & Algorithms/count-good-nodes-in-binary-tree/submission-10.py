# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stk = [(root, float("-inf"))]
        goodnodes = 0

        while stk:

            node, max_so_far = stk.pop()

            if node.val >= max_so_far:
                goodnodes += 1

            max_so_far = max(node.val, max_so_far)

            if node.right: stk.append((node.right, max_so_far))
            if node.left: stk.append((node.left, max_so_far))
        
        return goodnodes
            
            
            