class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        k = 3
            L
                R
        0 1 2 3 4 5 6
        1,6,1,0,4,2,6
        -----

        q = []

        pseudocode:
        - while q and num > q[-1]: pop
        - if L > q[0]: q.popleft
        - (R-L) + 1 == k: increment L += 1, take the q[0] which is the max

        O(n * m)
        """
        n = len(nums)
        q = deque()
        L = 0
        res = []

        for R in range(n):

            while q and nums[R] > nums[q[-1]]:
                q.pop()

            q.append(R)

            if L > q[0]:
                q.popleft()

            if ((R-L) + 1) == k:
                res.append(nums[q[0]])
                L += 1
        
        return res

