# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findmin(self,root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        """
        - Search for the value using binary search (O(logn))
        - If node found
            - Check if two children or one
            - If one children can directly delete and return the child
            - If two children then find min in the right subtree and replace it.
        """

        if not root:
            return
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else:

            if not root.left:
                return root.right
            
            if not root.right:
                return root.left
            
            else:
                minn_node = self.findmin(root.right)
                root.val = minn_node.val
                root.right = self.deleteNode(root.right, minn_node.val)
            
        return root

