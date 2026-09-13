"""        i
coins = [1,5,10], amount = 12                      

                            [1]                                                    [0]
                        
            [1,1]                               [1]                     [5]                            [0]

    [1,1,1]              [1,1]               [1,5]         [1]        [5,5]       [5]                    [10]        [0]
 
[1,1,1,1]   [1,1,1,]   [1,1,5]      [1,1]           

#base cases
if summ == amount:
    return 1

if summ > amount:
    return 0

if i >= len(coins):
    return 0

res = float("inf")

TC : O(2**n)

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        
        def dfs(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]
            
            if i >= len(coins):
                return float("inf")
            
            if summ == amount:
                return 0
            
            if summ > amount:
                return float("inf")

            #choose the number at i
            include = 1 + dfs(i, summ + coins[i])

            #don't choose
            skip = dfs(i+1, summ)

            cache[(i,summ)] = min(include, skip)

            return cache[(i,summ)]


        if dfs(0,0) == float("inf"):
            return -1 
        
        else:
            return dfs(0,0)

























