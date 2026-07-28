# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        """
        preorder - node, left, right
        inorder - left, node, right
        postorder

        O(n)
        O(n)
        """

        node_vals = []

        def dfs(root):

            if not root:
                return
            
            dfs(root.left)
            node_vals.append(root.val)
            dfs(root.right)
        
        dfs(root)

        print(node_vals)

        return node_vals[k-1]
