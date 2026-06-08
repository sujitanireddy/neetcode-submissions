# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stk = []

        def inorder_dfs(root):

            nonlocal stk

            if not root:
                return None
            
            inorder_dfs(root.left)
            stk.append(root.val)
            inorder_dfs(root.right)
        
        inorder_dfs(root)

        return stk[k-1]

