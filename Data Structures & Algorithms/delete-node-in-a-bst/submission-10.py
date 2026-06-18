# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def find_min(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        #searching for the key O(logn)

        #if key is found
            #No children or 1 child: delete diretly and return
            #if two children. Find the left most node in the right subtree and replace with root val and delete
        
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else:
            if not root.right and not root.left:
                return None

            elif not root.right:
                return root.left
            
            elif not root.left:
                return root.right
            
            else:
                min_node = self.find_min(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        
        return root

