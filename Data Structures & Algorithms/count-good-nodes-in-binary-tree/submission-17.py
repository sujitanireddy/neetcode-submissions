# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stk = [(root, root.val)]
        goodNodes = 0
        
        while stk:
            node, max_val = stk.pop()

            if node.val >= max_val:
                goodNodes += 1
                max_val = node.val
            
            if node.right: stk.append((node.right, max_val))
            if node.left: stk.append((node.left, max_val))
        
        return goodNodes
