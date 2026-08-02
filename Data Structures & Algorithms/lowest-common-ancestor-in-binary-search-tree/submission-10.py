# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        """
        What is the subproblem?
        - If both p and q values are less then look in the left subtree
        - If both p and q values are greter then look in the right subtree
        - return the root val

        Base Case:
        if root.val == p or root.val == q: return root.val
        """

        if p.val == root.val or q.val == root.val:
            return root
        
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return root
        

