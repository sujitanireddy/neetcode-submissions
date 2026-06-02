# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_d = 0

        def depthofBinaryTree(root):

            nonlocal max_d

            if not root:
                return 0

            max_d = max(max_d, (depthofBinaryTree(root.left) + depthofBinaryTree(root.right)))
            
            return max(depthofBinaryTree(root.left), depthofBinaryTree(root.right)) + 1
        
        depthofBinaryTree(root)

        return max_d