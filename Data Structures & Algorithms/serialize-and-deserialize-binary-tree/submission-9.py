# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        #preorder: Root -> left -> right

        nodes = []

        def dfs(root):

            if not root:
                nodes.append("N")
                return
            
            nodes.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        
        return (",").join(nodes)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        nodes = data.split(",")
        self.i = 0

        def dfs():

            if nodes[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(nodes[self.i])
            self.i += 1
            root.left = dfs()
            root.right = dfs()

        dfs()

        return root
