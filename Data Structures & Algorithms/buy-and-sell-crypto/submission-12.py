class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #algorithm
        #If the R pointer's price is ever lower than the left pointer move the R to L
        #Keep tracking the running max_p and return after R is out of bounds

        max_p = 0
        n = len(prices)
        L = 0
        R = n - 1

        for R in range(n):

            if prices[R] < prices[L]:

                L = R

            max_p = max(max_p, (prices[R] - prices[L]))
        
        return max_p