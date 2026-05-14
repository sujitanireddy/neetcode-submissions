class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #alogrithm
        # Using sliding window algorithm.
        # If we go pass the window. Pop left from the q so that we are not accounting for flase positives
        # if we hit window limit. Move L pointer and add the left most element ot the output 

        output = []
        q = deque()
        L = 0

        for R in range(len(nums)):

            while q and nums[q[-1]] < nums[R]:
                q.pop()

            q.append(R)

            while L > q[0]:
                q.popleft()

            if ((R - L) + 1) == k:

                output.append(nums[q[0]])

                L += 1

        return output  