"""
preorder -> root -> left -> right
inorder -> left -> root -> right

                                
            i                           
            0 1 2 3                       
preorder = [1,2,3,4]

            L     
           R
           0 1 2 3
inorder = [2,1,3,4]



            1

        

hashmap: to store the indexes and values of inorder

{
    1 : 1 #value: idx
}

Notes
- Global varibable for tracking i
- Will pass L,R into recursive DFS funtion.

TC: O(n) 
SC: O(n)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_val_idx_map = {v:i for i, v in enumerate(inorder)}
        self.preorder_idx = 0

        def dfs(L,R):
            
            while L <= R:
                
                val = preorder[self.preorder_idx]
                root = TreeNode(val)
                self.preorder_idx += 1
                mid = inorder_val_idx_map[val]

                root.left = dfs(L, mid-1)
                root.right = dfs(mid+1, R)

                return root

        return dfs(0,len(inorder) - 1)
        





