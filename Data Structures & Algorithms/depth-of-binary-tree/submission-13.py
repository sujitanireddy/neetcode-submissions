# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        """
        Recursive

        Basecase
        - if not root: return 0

        As we go depper we keep adding the depth

        """
        q = deque()
       
        if root:
            q.append(root)
        else:
            return 0

        levels = 0

        while q:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            levels +=1 

        return levels
            



