"""
 0 1 2
[1,2,3]

cost[i] + min(dp[i+2], dp[i+1])

f(n) = cost[i] + min(f(i+1), f(i+2))

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+2], cost[i+1])
        
        return min(cost[0], cost[1])