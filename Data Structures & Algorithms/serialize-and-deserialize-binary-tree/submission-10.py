# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        #postorder traversal
        self.vals = []

        def post_order_dfs(root):

            if not root:
                self.vals.append("N")
                return
            
            self.vals.append(str(root.val))
            post_order_dfs(root.left)
            post_order_dfs(root.right)

        post_order_dfs(root)
        return (",").join(self.vals)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        self.i = 0
        self.vals = data.split(",")

        print(self.vals)

        def post_order_dfs(root):

            if self.vals[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(self.vals[self.i])
            self.i += 1
            root.left = post_order_dfs(self.vals[self.i])
            root.right = post_order_dfs(self.vals[self.i])
        
        return root


            