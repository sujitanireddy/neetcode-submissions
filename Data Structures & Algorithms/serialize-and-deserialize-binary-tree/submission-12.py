# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
preorder: root -> left -> right 
1,2,3,4,5

[1,2,N,N,3,4,N,N,5,N,N]
"1,2,3,4,5"

[1,2,3,4,5]
"""
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        output = []

        def dfs(root):

            if not root:
                output.append("N")
                return
            
            output.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return ",".join(output)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(",")

        def dfs(i):

            if vals[i] == "N":
                return None

            root = TreeNode(int(vals[i]))
            root.left = dfs(i+1)
            root.right = dfs(i+1)

        dfs(0)

        return root



            



