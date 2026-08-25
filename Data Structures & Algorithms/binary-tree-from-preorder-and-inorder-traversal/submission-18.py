# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

preorder: node -> left -> right
inorder: left -> node -> right
postorder: left -> right -> node

            i
preorder = [1,2,3,4]
            R 
            L  1
inorder =  [2,1,3,4]

inorder_idx_map: { val: idx}

"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_idx_map = {v : i for i, v in enumerate(inorder)}

        self.preorder_idx = 0

        def dfs(L,R):

            if L > R:
                return None

            val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            root = TreeNode(val)
            mid = inorder_idx_map[val]

            root.left = dfs(L, mid - 1)
            root.right = dfs(mid + 1, R)
        
            return root
        
        return dfs(0, len(inorder) - 1)

