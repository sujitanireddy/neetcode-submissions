# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        """

        Recursively 

        - What is the max path that you can achive - asking left and right subtree
        

        Base case - if not root: return 0
        At every node the max_diameter = left_path + right+path
        promote the max of left,right

        """

        max_diameter = [0]

        def depth(root):

            if not root:
                return 0 
            
            left_depth = depth(root.left)
            right_depth = depth(root.right)

            max_diameter[0] = max(max_diameter[0], left_depth + right_depth)

            return 1 + max(left_depth, right_depth)
        
        depth(root)

        return max_diameter[0]
