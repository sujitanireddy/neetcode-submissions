class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}
        
        def dfs(i):

            if i in cache:
                return cache[i]
            
            if i >= len(cost):
                return 0
            
            cache[i] = min(dfs(i+1), dfs(i+2)) + cost[i]

            return cache[i]
        
        dfs(0)
        dfs(1)
        
        return min(cache[0], cache[1])