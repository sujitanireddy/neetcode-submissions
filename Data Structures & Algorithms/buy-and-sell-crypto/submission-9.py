class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        L = 0
        max_price_seen = float("-inf")

        for R in range(0, len(prices)):

            if prices[R] < prices[L]:

                L = R 
            
            else:
                
                price = prices[R] - prices[L]

                max_price_seen = max(max_price_seen, price)
        
        return max_price_seen if max_price_seen != float("-inf") else 0 


        
        