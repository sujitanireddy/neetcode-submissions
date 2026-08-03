class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
                   L
                   R          
        10,1,5,6,7,1

        if price drops then we buy at that new dropped price.
        """
        L = 0
        max_p = 0

        for R in range(len(prices)):

            if prices[R] < prices[L]:
                L = R
            
            max_p = max(max_p, prices[R] - prices[L])
        
        return max_p
