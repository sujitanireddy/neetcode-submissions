"""
     r
[2,1,1,2]

f(i) = max(nums[i] + f(i+2), f(i+1))

"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = {}
        
        def recurse(n):

            if n >= len(nums):
                return 0
            
            if n in cache:
                return cache[n]
            
            cache[n] = max((nums[n] + recurse(n+2)), recurse(n+1))

            return cache[n]

        return recurse(0)

            

        