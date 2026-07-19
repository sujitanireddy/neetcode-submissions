# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = [0]
        
        def depth(root):

            if not root:
                return 0
            
            max_left = depth(root.left)
            max_right = depth(root.right)
            
            diameter[0] = max(diameter[0], max_left + max_right)
            
            return 1 + max(max_left, max_right)
        
        depth(root)

        return diameter[0]
        

        
