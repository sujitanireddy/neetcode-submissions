"""           i                  L     
                                 R
                                 0 1 2 3        
preorder = [1,2,3,4], inorder = [2,1,3,4]

inorder_value_idx_map: {idx:val}

                    1
                 
 if L > R:

inorder: left -> root -> right
preorder: root -> left -> right
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_val_idx_map = {val:i for i, val in enumerate(inorder)}
        self.preorder_idx = 0
    
        def dfs(L,R):

            while L <= R:
            
                val = preorder[self.preorder_idx]
                root = TreeNode(val)
                mid = inorder_val_idx_map[val]
                self.preorder_idx += 1

                root.left = dfs(L, mid - 1)
                root.right = dfs(mid+1, R)

                return root

        return dfs(0,len(inorder)-1)








