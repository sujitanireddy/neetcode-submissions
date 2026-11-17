"""
                                                0                                
                                     1                                   0
                                
                                1+1                1                5         0  
    
                          1+1+1       1+1       1+5     1       5+5     5   10      0

                    1+1+1+  
Base case:
- if summ
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}

        def dfs(i,summ):

            if (i,summ) in cache:
                return cache[(i,summ)]

            if i >= len(coins):
                return float("inf")
            
            if summ > amount:
                return float("inf")

            if summ == amount:
                return 0

            #choose
            choose = 1 + dfs(i, summ + coins[i])

            #skip
            skip = dfs(i+1, summ)

            cache[(i,summ)] = min(choose, skip)

            return cache[(i,summ)]

        res = dfs(0, 0)

        return res if res != float("inf") else -1