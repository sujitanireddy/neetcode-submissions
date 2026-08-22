"""
i   
1,2,3

i
1,2,1,2,1,1,1

f(i) = cost[i] + min(f(i+1), f(i+2)) 

base case: i >= len(cost): return 0

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cache = {}

        def recurse(i):

            if i >= len(cost):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(recurse(i+1), recurse(i+2))

            return cache[i]

        recurse(0)

        return min(cache[0],cache[1])
