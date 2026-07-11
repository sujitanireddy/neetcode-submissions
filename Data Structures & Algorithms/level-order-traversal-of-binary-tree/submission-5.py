# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        """
        BFS = queue 
        TC: O(n) where n is the no of nodes.
        """
        q = deque()
        
        if root:
            q.append(root)
        else:
            return []
        
        res = []

        while q:
            sol = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                sol.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(sol)
        
        return res


