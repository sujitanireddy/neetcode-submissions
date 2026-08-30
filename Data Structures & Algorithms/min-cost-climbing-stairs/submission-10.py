class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        cache = {}

        def recurse(i):

            if i in cache:
                return cache[i]

            if i >= n:
                return 0
            
            cache[i] = cost[i] + min(recurse(i+1), recurse(i+2))

            return cache[i]

        recurse(0)

        return min(cache[0],cache[1])

