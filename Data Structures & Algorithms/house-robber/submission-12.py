"""
1 1 3 3

  R   R
2,9,8,3,6

f(i) = max(nums[i] + f(i+2), f(i+1))

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        cache = {}

        def recurse(i):

            if i in cache:
                return cache[i]
            
            if i >= len(nums):
                return 0
            
            cache[i] = max(nums[i] + recurse(i+2), recurse(i+1))

            return cache[i]

        return recurse(0)






