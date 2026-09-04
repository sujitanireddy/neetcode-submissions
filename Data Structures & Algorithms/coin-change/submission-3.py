"""
                                          1 5 10
                        
                         1                   5                        10

                 2       6      11     6    10     15X         11     15X     20X
        
        3       5     12 (return 1)

base cases:
- if summ == amount: return 1
- if summ > amount:  return 0

BruteForce:
TC: O(2**n)
SC: O(h)

Top Down memoized:
TC: O(n)
SC: O(n)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        
        def dfs(summ):

            if summ in cache:
                return cache[summ]
            
            if summ == amount:
                return 0
            
            if summ > amount:
                return float("inf")
            
            min_coins = float("inf")
            
            for coin in coins:
                min_coins = min(min_coins, 1 + dfs(coin + summ))

            cache[summ] = min_coins

            return min_coins

        res = dfs(0)


        if res == float("inf"):
            return -1
        else:
            return res