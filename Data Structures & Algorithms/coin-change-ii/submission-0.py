"""
- unbounded knapsack
base case: if summ == amount: return 1
           if i >= len(coins): return 0

"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}
        
        def dfs(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]

            if summ == amount:
                return 1

            if i >= len(coins):
                return 0
            
            if summ > amount:
                return 0

            res = 0
            
            #skip
            res += dfs(i+1, summ)

            #choose
            res += dfs(i, summ + coins[i])

            cache[(i,summ)] = res

            return res
        
        return dfs(0,0)