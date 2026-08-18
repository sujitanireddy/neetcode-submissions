"""
preorder : node -> left -> right (order)
inorder : left -> node -> right (struct)
postorder: left -> right -> node

              i        
preorder = [1,2,3,4]
            
           
          L m
            L m   R
inorder =  [2,1,3,4]

inorder_val_idx map {2:0, 1:1, 3:2, 4:3} 

                             1 
                          2
                           
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_val_idx = {v : i for i, v in enumerate(inorder)}
        self.preorder_idx = 0

        def dfs(L,R):
            
            if L > R: 
                return None

            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            mid = inorder_val_idx[root_val] 
            self.preorder_idx += 1
            
            root.left = dfs(L, mid-1)
            root.right = dfs(mid+1, R)

            return root


        return dfs(0,len(preorder)-1)

