# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        val_idx_map = defaultdict(int)
        for i, v in enumerate(inorder):
            val_idx_map[v] = i
        
        self.preidx = 0

        def dfs(L,R):

            if L > R:
                return None

            root_val = preorder[self.preidx]
            root = TreeNode(root_val)
            self.preidx += 1
            mid = val_idx_map[root_val]

            root.left = dfs(L, mid -1)
            root.right = dfs(mid+1, R)

            return root

            




        
        return dfs(0, len(preorder) - 1)
