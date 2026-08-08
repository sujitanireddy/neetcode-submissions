# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        preorder: node -> left -> right
        inorder: left -> node -> right
                                           L 
                                                 R     
        preorder =  1,2,3,4     inorder =  2,1,3,4 

        inorder_val_idx_map
        {
            2 : 0
            1 : 1
            3 : 2
            4 : 3
        }       

        L > R: return None
        """

        val_idx_map = defaultdict(int)
        for i, v in enumerate(inorder):
            val_idx_map[v] = i

        self.preorder_idx = 0
        
        def dfs(L,R):
            
            if L > R:
                return None
            
            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            self.preorder_idx += 1
            mid = val_idx_map[root_val]

            root.left = dfs(L, mid-1)
            root.right = dfs(mid+1, R)

            return root


        return dfs(0,len(preorder)-1)

        