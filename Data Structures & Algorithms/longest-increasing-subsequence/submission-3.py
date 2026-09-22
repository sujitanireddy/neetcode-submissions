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

        dp = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):

                if nums[i] < nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)