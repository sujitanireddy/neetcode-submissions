class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(len(prices)):
            
            buy_stock = prices[i]

            for j in range(i+1, len(prices)):

                sell_stock = prices[j]

                profit = max(profit, sell_stock - buy_stock)

        return profit