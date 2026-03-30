class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = 0
        max_profit_seen = 0

        for R in range(1, len(prices)):

            if prices[R] < prices[L]:

                L = R
            
            elif prices[R] > prices[L]:

                max_profit_seen = max(max_profit_seen, (prices[R] - prices[L]))
        
        return max_profit_seen

