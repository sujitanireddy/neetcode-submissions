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
        delimiter = ","
        
        def preorder_dfs(root):

            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            preorder_dfs(root.left)
            preorder_dfs(root.right)
        
        preorder_dfs(root)
        
        print(res)

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        delimiter = ","
        vals = data.split(delimiter)
        self.i = 0
        
        def preorder_dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            node.left = preorder_dfs()
            node.right = preorder_dfs()

            return node
        
        return preorder_dfs()

        
