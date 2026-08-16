class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        cache = {}
        
        def recurse(i):

            if i >= len(nums) - 1:
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + recurse(i+2), recurse(i+1))

            return cache[i]
        

        cache_one = {}

        def recurse_one(i):

            if i >= len(nums):
                return 0
            
            if i in cache_one:
                return cache_one[i]
            
            cache_one[i] = max(nums[i] + recurse_one(i+2), recurse_one(i+1))

            return cache_one[i]
        
        
        return max(recurse(0), recurse_one(1))
 
        
        