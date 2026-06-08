# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stk = []

        def postorder_dfs(root):

            nonlocal stk

            if not root:
                return
            
            postorder_dfs(root.left)
            postorder_dfs(root.right)
            stk.append(root.val)
        
        postorder_dfs(root)

        return stk