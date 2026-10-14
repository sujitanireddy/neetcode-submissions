"""
[1,5,10]    

Base case:
if summ == amount:
    return 0

if summ > amount:
    return 0

add 1 whenever we are choosing and accumulate the min

TC: 2 * amount/min_coin
SC: amount/min_coin

Top down memoization:
TC: O(m*n)
SC: O(m*n)

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        
        def dfs(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]

            if i >= len(coins):
                return float("inf")

            if summ == amount:
                return 0
            
            if summ > amount:
                return float("inf")
            
            res = min(1 + dfs(i, summ + coins[i]), dfs(i+1, summ))

            cache[i,summ] = res

            return res

        res = dfs(0,0)

        if res == float("inf"):
            return -1
        else:
            return res  