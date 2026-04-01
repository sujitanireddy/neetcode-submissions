class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #algorithm
        #L = 0, for every num if top of q[-1] < num. q.pop()
        #store the index of the num
        #if the q[0] > L: popleft()
        #if (R - L) + 1 == k:
            #ouptput.append(q[0])
            #L+=1
        
        L = 0
        q = deque()
        output = []

        for R in range(len(nums)):

            while q and nums[q[-1]] < nums[R]:
                q.pop()
            
            q.append(R)

            if L > q[0]:
                q.popleft()

            if (R - L) + 1 == k:

                output.append(nums[q[0]])

                L += 1
        
        return output