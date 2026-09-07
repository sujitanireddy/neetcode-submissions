"""
             
0 1 2 
1,2,3
                      
1,2,1,2,1,1,1

TC: O(2**n)
SC: O(h)

Recurence Relation
f(n) = cost[i] + min(f(i+1), f(i+2))
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}

        def recurse(i):
            
            if i in cache: 
                return cache[i]

            if i >= len(cost): 
                return 0
            
            cache[i] = cost[i] + min(recurse(i+1), recurse(i+2))

            return cache[i]

        recurse(0)

        return min(cache[0], cache[1])
        