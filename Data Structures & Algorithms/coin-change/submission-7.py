class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        
        def recurse(summ):

            if summ in cache:
                return cache[summ]
        
            if summ > amount:
                return float("inf")
            
            if summ == amount:
                return 0
            
            res = float("inf")
            
            for coin in coins:
                res = min(res, 1 + recurse(coin + summ))

            cache[summ] = res
            
            return res
        
        result = recurse(0)

        if result == float("inf"):
            return -1
        else:
            return result

    
