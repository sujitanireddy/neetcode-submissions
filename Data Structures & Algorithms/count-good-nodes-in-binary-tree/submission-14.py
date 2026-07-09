# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        """
        dfs, bfs
        recursive or iterative way

                                          2
                                  1               1

                            3                1         5

        stk = [(root)]
        [1, 1]
        """
        if root:
            stk = [(root, float("-inf"))]
        
        good_nodes = 0
        
        while stk:
            node, maxx = stk.pop()

            if node.val >= maxx:
                good_nodes += 1
            
            maxx = max(maxx, node.val)
        
            if node.right: stk.append((node.right, maxx))
            if node.left: stk.append((node.left, maxx))
        
        return good_nodes