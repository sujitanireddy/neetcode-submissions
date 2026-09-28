"""
early return case:
if not root:
    return 0

            1 +1        (1) max(left, right) 
        
       1 2      1 3



            4 + 1

TC : O(n)
SC : O(h)


stk[]


                [(




h = 0


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque()
        q.append(root)
        level = 0

        while q:

            length = len(q)
            level += 1

            for i in range(length):

                node = q.popleft()

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return level














