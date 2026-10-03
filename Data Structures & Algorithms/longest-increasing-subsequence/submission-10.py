"""
[9,1,4,2,3,3,7]


2






"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = {}
        
        def recurse(i, prev):

            if (i,prev) in cache:
                return cache[(i,prev)]
            
            if i >= len(nums):
                return 0

            LIS = float("-inf")

            #don't choose
            LIS = recurse(i+1, prev)
            
            #choose
            if nums[i] > prev:
                LIS = max(LIS, 1 + recurse(i+1, nums[i]))

            cache[(i,prev)] = LIS
            
            return LIS

        return recurse(0,float("-inf"))