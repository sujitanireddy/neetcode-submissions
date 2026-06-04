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
        
        if not root:
            return
        
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
                min_node = self.find_min(root.right)
                print(min_node.val)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root