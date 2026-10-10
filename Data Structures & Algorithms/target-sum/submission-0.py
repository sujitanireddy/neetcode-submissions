"""
base case:
- if i > len(nums):
    return 0
- if i == len(nums) and summ == target:
    return 1

choose 

skip
Brute Force approach
TC : O(2**n)
SC : O(n)
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}
        
        def recurse(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]
            
            if i == len(nums) and summ == target:
                return 1
            
            if i >= len(nums):
                return 0
            
            cache[(i,summ)] = recurse(i+1, summ + nums[i]) + recurse(i+1, summ - nums[i])

            return cache[(i,summ)]

        return recurse(0,0)