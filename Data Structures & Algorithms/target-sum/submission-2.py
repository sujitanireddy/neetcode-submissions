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

Top down memoization
TC : O(n*m)
SC : O(n*m)

Bottom up dynamic programming sol:
TC : O(n*m)
SC : O(1)

  0 {0:1}
2 1
2 2
2 3

"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = [defaultdict(int) for _ in range(len(nums)+1)]

        dp[0][0] = 1

        for i in range(len(nums)):
            for summ, count in dp[i].items():

                dp[i+1][summ + nums[i]] += count
                dp[i+1][summ - nums[i]] += count
        
        return dp[len(nums)][target]
