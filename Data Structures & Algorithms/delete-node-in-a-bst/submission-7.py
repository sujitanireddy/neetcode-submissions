# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findmin(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        #search for the key node
        
        #base case
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            else:
                right_min_node = self.findmin(root.right)
                root.val = right_min_node.val
                root.right = self.deleteNode(root.right, right_min_node.val)

        return root 

            
        