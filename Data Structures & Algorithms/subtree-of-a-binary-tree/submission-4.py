# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False

        def issametree(root, subRoot):

            if not root and not subRoot:
                return True
            
            if (root and not subRoot) or (subRoot and not root):
                return False
            
            if root.val != subRoot.val:
                return False
            
            return issametree(root.left, subRoot.left) and issametree(root.right, subRoot.right)

        return issametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)