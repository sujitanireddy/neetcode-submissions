"""
Recursion
 
   i
[1,5,10]                               start of recursion

                                   [1]                         []

                          [1,1]             [1]             [5]           []
                        
                   [1,1,1]              [1,5]   [1]    [1]     [5,5]   [5] ....

            [1,1,1,1]   [1,1,1]    [1,5,10]        

Base Case:
- if summ == amount:
        return 0 
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        
        def dfs(i,summ):

            if (i,summ) in cache:
                return cache[(i,summ)] 
            
            if summ > amount:
                return float("inf")

            if summ == amount:
                return 0

            if i >= len(coins):
                return float("inf")
            
            #skip the coin
            skip = dfs(i+1, summ)

            #include the coin
            include = 1 + dfs(i, coins[i] + summ)
            
            res = min(skip, include)

            cache[(i,summ)] = res

            return res

        ans = dfs(0,0) #index, summ

        if ans == float("inf"):
            return -1
        else:
            return ans