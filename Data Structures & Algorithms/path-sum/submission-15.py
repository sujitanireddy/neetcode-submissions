"""
              -15 (0)
               
               
        10 (-10)      20 (20)

                     15 (35)   5 (15)

                    -5 (30)
                    

if not root:
    return 0

if (root.val + prevSum) == targetSum:
    return True

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        stk = [(root, 0)]

        while stk:
            node, summ = stk.pop()

            summ = node.val + summ

            if not node.left and not node.right and summ == targetSum:
                return True

            if node.right: stk.append((node.right, summ))
            if node.left: stk.append((node.left, summ))
        
        return False

        