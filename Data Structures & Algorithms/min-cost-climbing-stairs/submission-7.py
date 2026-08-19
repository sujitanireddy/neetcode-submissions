"""

1  2  3
           0     0   
  min(1 + f(2), f(1))
                  
            
 

Brute Force approach:
f(i) = min(cost[i] + f(i+2), f(i+1))

cache
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for i in range(len(cost)-3, -1 ,-1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1]) 
