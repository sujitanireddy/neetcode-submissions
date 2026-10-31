class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        L = 0

        for R, n in enumerate(nums):

            while q and nums[q[-1]] < n:
                q.pop()
            
            q.append(R)

            if q and L > q[0]:
                q.popleft()

            
            
            if (R - L) + 1 == k:
                res.append(nums[q[0]])
                L += 1 
        
        return res