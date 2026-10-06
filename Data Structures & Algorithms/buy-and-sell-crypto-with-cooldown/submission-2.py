"""







"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}
        
        def dfs(i, can_buy):

            if (i,can_buy) in cache:
                return cache[(i,can_buy)]

            if i >= len(prices):
                return 0

            cooldown = dfs(i+1, can_buy)
            
            if can_buy:
                res = max(cooldown, dfs(i+1, False) - prices[i])
            
            else:
                res = max(cooldown, dfs(i+2, True) + prices[i])

            cache[(i,can_buy)] = res
            
            return cache[(i,can_buy)]
        
        return dfs(0,True)