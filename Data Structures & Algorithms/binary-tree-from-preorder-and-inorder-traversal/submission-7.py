# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        """
        dfs = preorder, inorder, postorder
        preorder: root -> left -> right
        inorder: left -> root -> right
        postorder: left -> right -> root
                                         0 1 2 3
        preorder = [1,2,3,4], inorder = [2,1,3,4]


        #basecase
        if not preorder or inorder:
            return

        root = preorder[0]
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder = preorder[mid: mid+1], inorder = inorder[:mid])
        root.right = self.buildTree(preorder = preorder[mid+1:], inorder = inorder[mid+1:])
        """

        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        print(preorder[mid: mid+1])
        root.left = self.buildTree(preorder = preorder[1: mid+1], inorder = inorder[:mid])
        root.right = self.buildTree(preorder = preorder[mid+1:], inorder = inorder[mid+1:])

        return root