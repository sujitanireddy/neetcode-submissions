class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        """
           L
               R
        [1,2,1,0,4,2,6]

        [1]

        """

        L = 0
        q = deque()
        res = []

        for R in range(len(nums)):

            while q and nums[q[-1]] < nums[R]:
                q.pop()

            q.append(R)

            if L > q[0]:
                q.popleft()


            if (R - L) + 1 == k:
                res.append(nums[q[0]])
                L += 1
        
        return res