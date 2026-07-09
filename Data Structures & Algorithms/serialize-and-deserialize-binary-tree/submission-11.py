# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
dfs - Preorder traveral = root, left, right

base case:
if nulll: "N"

"""

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        vals = []

        def preorder_dfs(root):

            if not root:
                vals.append("N")
                return
            
            vals.append(str(root.val))
            preorder_dfs(root.left)
            preorder_dfs(root.right)

        preorder_dfs(root)

        return "".join(vals)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        i = 0

        def preorder_dfs(i):

            if data[i] == "N":
                i += 1
                return None
            
            if i == len(data):
                return
            
            root = TreeNode(data[i])
            root.left = TreeNode(data[i+1])
            root.right = TreeNode(data[i+1])
        
        preorder_dfs(0)

        return root

