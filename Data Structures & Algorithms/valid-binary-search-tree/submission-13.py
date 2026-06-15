# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stk = []

        if root:
            stk.append((root, float("-inf"), float("inf"))) #(node, min, maxx)

        while stk:

            node, minn, maxx = stk.pop()

            if not minn < node.val < maxx:
                return False

            if node.right: stk.append((node.right, node.val, maxx))
            if node.left: stk.append((node.left, minn, node.val))
        
        return True