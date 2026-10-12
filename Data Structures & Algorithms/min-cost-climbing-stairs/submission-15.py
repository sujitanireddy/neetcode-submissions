"""
 0 1 2
[1,2,3]
     
 0 1 2 3
 3 2 3 0

cost[i] + min(dp[i+2], dp[i+1])

f(n) = cost[i] + min(f(i+1), f(i+2))

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0] * (len(cost) + 1)
        dp[len(cost)-1] = cost[len(cost)-1]

        for i in range(len(cost) - 2, -1, -1):
            dp[i] = cost[i] + min(dp[i+2], dp[i+1])
        
        return min(dp[0],dp[1])