class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        """
        0 1  2 3 4 5 6
                 R 
             L
        1 10 1 0 4 2 6

        q = [1,2,3]

        res = [10,10]

        0 1 2
            r
          l
        7,2,4]
        k=2. 

        q = [0,1]

        res = [7,]

        we can use a queue to hold the max so far, but remove from q if the value is not in the window.
        capture the index in the q, this will make the implementation easier
        """
        q = deque()
        L = 0
        res = []

        for R in range(len(nums)):

            while q and nums[R] > nums[q[-1]]:
                q.pop()

            q.append(R)

            if L > q[0]:
                q.popleft()
            
            if ((R - L) + 1) == k:
                res.append(nums[q[0]])
                L += 1



        return res

            