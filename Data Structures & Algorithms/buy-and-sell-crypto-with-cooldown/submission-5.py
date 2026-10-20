"""
TC: O(2**n)
SC: O(n)

[1,3,4,0,4]








- You can either buy or sell
- If you sell, cannot buy the next day

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:  

        cache = {}

        def dfs(i, canBuy):

            if (i,canBuy) in cache:
                return cache[(i,canBuy)]
            
            if i >= len(prices):
                return 0

            buy = sell = 0

            if canBuy:
                buy = dfs(i+1, False) - prices[i]
            
            else:
                sell = dfs(i+2, True) + prices[i]

            cooldown = dfs(i+1, canBuy)
        
            cache[(i,canBuy)] = max(buy, sell, cooldown)

            return cache[(i,canBuy)]

        return dfs(0, True)