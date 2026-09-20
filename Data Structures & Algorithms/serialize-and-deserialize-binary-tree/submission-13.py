"""
Early return case: if not root: return N

DFS - Inorder Traversal O(n) : left -> node -> right

[1,2,N,N,3,4,N,N,5,N,N]

 i
[N,2,N,1,N,4,N,3,N,5,N]


            1
        2         3
    N       N   4     5

            n    n  n      n

for None node = 'N'
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []

        def dfs(node):
            
            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        res = data.split(',')
        self.i = 0

        def dfs():

            if self.i >= len(res):
                return None
            
            if res[self.i] == 'N':
                self.i += 1
                return None
            
            root = TreeNode(res[self.i])
            self.i += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()


