class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        cache = {}
        
        def dfs(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]

            if len(nums) == i and summ == target:
                return 1

            if i >= len(nums):
                return 0

            cache[(i,summ)] = dfs(i+1, summ - nums[i]) + dfs(i+1, summ + nums[i])

            return cache[(i,summ)]

        return dfs(0,0)