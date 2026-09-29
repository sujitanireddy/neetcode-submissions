"""
        L
            R
1,2,1,0,4,2,6
-----

q = [4]
res = [2,2,4,4,6]

Notes:

- store indexs in q

- if we see a larger value:
    popleft() and add larger value

- if we move our left pointer:
    the index of the q is < L pointer then remove it

TC: O(n)
SC: O(n)

    L
        R
0 1 2 3 4 5 6
1,2,1,0,4,2,6


2 > 1


q = [4]

res = [2]
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = deque()
        res = []
        L = 0

        for R, num in enumerate(nums):

            while q and num > nums[q[-1]]:
                q.pop()

            q.append(R)

            if q[0] < L:
                q.popleft()
            
            #if we match the window size
            if (R - L) + 1 == k:
                res.append(nums[q[0]])
                L += 1

        return res









































