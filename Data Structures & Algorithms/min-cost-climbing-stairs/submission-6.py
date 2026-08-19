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
        
        cache = {}

        def recurse(i):

            if i in cache:
                return cache[i]

            if i >= len(cost):
                return 0
            
            cache[i] = cost[i] + min(recurse(i+2), recurse(i+1))

            return cache[i]

        recurse(0)
            
        return min(cache[0],cache[1])
