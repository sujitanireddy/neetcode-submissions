"""
early return case:
if not root:
    return 0

            1 +1        (1) max(left, right) 
        
       1 2      1 3



            4 + 1

TC : O(n)
SC : O(h)


stk[]


                [(




h = 0


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        stk = [(root, 1)]
        max_height = 1

        while stk:

            node, height = stk.pop()

            max_height = max(height, max_height)

            if node.right: stk.append((node.right, height + 1))
            if node.left: stk.append((node.left, height + 1))

        
        return max_height

