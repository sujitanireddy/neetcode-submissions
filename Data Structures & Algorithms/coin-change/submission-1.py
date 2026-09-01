"""
if summ == amount: return count 


count = i? 
summ


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
                return float('inf')

            res = float('inf')

            for c in coins:
                res = min(res, 1 + dfs(c + summ))

            cache[summ] = res

            return res

        result = dfs(0)

        return result if result != float('inf') else -1
            




