"""
    i
1   5   10                             

                        1                   5                       10

                    1   5   10      1       5       10          1   5   10           

                1   5   10 

#base cases
if i >= len(coins):
    return float("inf")

if summ == amount:
    return 0

if summ > amount:
    return float("inf")
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        
        def dfs(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]

            if summ == amount:
                return 0

            if i >= len(coins):
                return float("inf")
            
            if summ > amount:
                return float("inf")

            cache[(i,summ)] =  min(dfs(i, summ + coins[i]) + 1, dfs(i+1, summ))

            return cache[(i,summ)]

        res = dfs(0,0)

        if res == float("inf"):
            return -1
        
        else:
            return res