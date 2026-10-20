"""         i
nums = [2,2,2], target = 2


Recursive Tree
                            0
            
              2                           -2

        4           0               0           -2

    6       2   2       -2      2       -2    0        -4 
    
Base case:
- if i >= len(nums):
    return 0
- if summ == target:
    return 1

"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}
        
        def dfs(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]

            if i == len(nums) and summ == target:
                return 1
            
            if i >= len(nums):
                return 0

            cache[(i,summ)] = dfs(i+1, summ + nums[i]) + dfs(i+1, summ - nums[i])

            return cache[(i,summ)]

        return dfs(0,0)