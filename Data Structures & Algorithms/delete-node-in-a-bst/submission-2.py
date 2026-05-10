# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def min_of_tree(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        #search for a node. 
            #if node found: check if node has 0, 1 or 2 children
                # for 0 and 1 children we can just return 
                # but for 2 children 
                    # find min in the right subtree
                    # replace the min val to root val
                    # recursivly delete the root.right subtree
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                min_node = self.min_of_tree(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
        return root
