"""         i
nums = [2,2,2], target = 2


Recursive Tree
                            {0:0}
            
              {2:1                           -2:1}

        {4:1           0:2               0           -2:1}

    {6:1       2   2       -2      2:3       -2:2    0:1        -4:1}
    
Base case:
- if i >= len(nums):
    return 0
- if summ == target:
    return 1

Top down memo sol:
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

Bottom up DP

                            {0:1}
            
              {2:1                           -2:1}

        {4:1           0:2               0           -2:1}

    {6:1       2   2       -2      2:3       -2:2    0:1        -4:1}
    

"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = [defaultdict(int) for _ in range(len(nums)+1)]

        dp[0][0] = 1

        for i in range(len(nums)):
            for summ, count in dp[i].items():

                dp[i+1][nums[i] + summ] += count
                dp[i+1][summ - nums[i]] += count

        return dp[len(nums)][target]









        