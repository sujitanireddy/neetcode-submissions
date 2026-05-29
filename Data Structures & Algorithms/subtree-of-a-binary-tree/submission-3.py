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
        
        if not subRoot:
            return True
        
        def sametree(root, subRoot):

            if not root and not subRoot:
                return True
            
            if (root and not subRoot) or (subRoot and not root):
                return False
            
            if root.val != subRoot.val:
                return False
            
            return sametree(root.left, subRoot.left) and sametree(root.right, subRoot.right)
        
        return sametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)