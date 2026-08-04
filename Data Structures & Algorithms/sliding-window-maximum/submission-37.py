class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        0 1 2 3 4 5 6 
        1 9 1 0 4 2 6    k = 3
              -

        q = [1]

        Condition: if q and nums[q[-1]] < n:
                        q.pop()
        
        if our L > q[0]: q.popleft()
        
        (R - L) + 1 = window size
        """
        q = deque()
        res = []
        L = 0
        
        for R in range(len(nums)):

            while q and nums[q[-1]] < nums[R]:
                q.pop()

            q.append(R)

            if L > q[0]:
                q.popleft()

            if (R - L) + 1 == k:
                res.append((nums[q[0]]))
                L += 1

        return res 


