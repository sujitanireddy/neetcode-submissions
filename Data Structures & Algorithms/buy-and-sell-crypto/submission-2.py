class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit_so_far = 0

        for i in range(len(prices)):

            for j in range(i+1, len(prices)):

                maxprofit_so_far = max(maxprofit_so_far, (prices[j] - prices[i]))

        return maxprofit_so_far


        