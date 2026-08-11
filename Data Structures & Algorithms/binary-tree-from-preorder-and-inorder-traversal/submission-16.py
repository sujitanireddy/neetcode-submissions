# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
                                          L
                                        R
        preorder [1,2,3,4]   inorder [2,1,3,4]

        inorder_map = {val:idx}
    
        """
        val_idx_map = defaultdict(int)
        for i, val in enumerate(inorder):
            val_idx_map[val] = i
        
        self.preorder = 0
        
        L = 0
        R = len(inorder) - 1

        def dfs(L,R):

            if L > R:
                return

            root_val = preorder[self.preorder]
            root = TreeNode(root_val)
            self.preorder += 1
            mid = val_idx_map[root_val]
            
            root.left = dfs(L, mid-1)
            root.right = dfs(mid+1, R)
            
            return root

        return dfs(L, R)