"""
0,3,1,3,2,3

9,1,4,2,3,3,7


start with min and keep incrementing if we found values greater than min?


9,1,4,2,3,3,7

0/1 knapsack 

if prev value is greater then cannot proceed that branch
if prev value is same then don't proceed with that branch
go until the end of the string
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = {}

        def recurse(i,prev):

            if (i,prev) in cache:
                return cache[(i,prev)]

            if i >= len(nums):
                return 0
            
            res = recurse(i+1, prev)

            if prev == float("-inf") or prev < nums[i]:
                res = max(res, 1 + recurse(i+1, nums[i]))
                cache[(i,prev)] = res
        
            return res

        return recurse(0,float("-inf"))