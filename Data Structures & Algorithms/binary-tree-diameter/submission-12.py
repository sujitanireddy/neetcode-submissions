# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        at every node, we calculate the left subtree height and right subtree height and save it.

        the max of this cummulative hegiht is what we return

           (1)
        0      1+(2) (max (left, right)
                      
             1+(3)   1+(4)
                     0    0
          1+(5)  0
         0  0
        """
        self.diameter = 0

        def dfs(root):
            
            if not root:
                return 0
            
            left_subtree_height = dfs(root.left)
            right_subtree_height = dfs(root.right)

            self.diameter = max(self.diameter, (left_subtree_height + right_subtree_height))

            return 1 + (max(left_subtree_height, right_subtree_height))

        dfs(root)
        return self.diameter