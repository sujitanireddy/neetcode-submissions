# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []
        q = deque()

        if root:
            q.append(root)

        while q:

            length = len(q)
            level = []

            for _ in range(length):

                node = q.popleft()
                
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            output.append(level)
        
        return output

