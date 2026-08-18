"""
search: O(logn)
delte a node: O(n)

TC: O(n)
SC: O(1)

Delete a node:
- if no children: return None
- if only 2 children: return child
- if two children: recursivly find the min node in teh right subtree and replace with root

        5
    2        7
 1    4   4   10
    2   5   N   N

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min(self,node):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        
        else:
            if root.left and not root.right:
                return root.left
            
            elif root.right and not root.left:
                return root.right
            
            elif not root.right and not root.left:
                return None
            
            else: 
                min_val = self.find_min(root.right)
                root.val = min_val
                root.right = self.deleteNode(root.right, min_val)

        return root
            


