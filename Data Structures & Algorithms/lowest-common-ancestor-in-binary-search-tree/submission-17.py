"""
DFS

Base case:
if not root:
    return None

if p.val == root.val or q.val == root.val:
    return root.val

if p.val > root.val and q.val > root.val:
    dfs(root.right)

if p.val < root.val and q.val < root.val:
    dfs(root.left)

TC: O(n)
SC: O(h)








"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node):
            
            if p.val > node.val and q.val > node.val:
                return dfs(node.right)

            elif p.val < node.val and q.val < node.val:
                return dfs(node.left)
            
            else:
                return node

        return dfs(root)



























