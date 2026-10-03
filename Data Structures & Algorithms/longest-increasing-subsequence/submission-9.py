"""
[9,1,4,2,3,3,7]


2






"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LIS = [float("-inf")]
        cache = {}
        
        def recurse(i, prev):

            if (i,prev) in cache:
                return cache[(i,prev)]
            
            if i >= len(nums):
                return 0

            #don't choose
            LIS[0] = recurse(i+1, prev)
            
            #choose
            if nums[i] > prev:
                LIS[0] = max(LIS[0], 1 + recurse(i+1, nums[i]))

            cache[(i,prev)] = LIS[0]
            
            return LIS[0]

        return recurse(0,float("-inf"))