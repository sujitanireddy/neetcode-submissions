# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stk = []

        def preorder_dfs(root):

            nonlocal stk

            if not root:
                return
            
            stk.append(root.val)
            preorder_dfs(root.left)
            preorder_dfs(root.right)
        
        preorder_dfs(root)
        
        return stk