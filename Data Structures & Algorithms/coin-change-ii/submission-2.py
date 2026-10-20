"""
[1,2,3]

- Recursive sol (unbounded knapsack)

Base Cases:
- out of bounds check
- target hit check
- summ over target hit

"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}
        
        def dfs(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]

            #base cases
            if i >= len(coins):
                return 0
            
            if summ == amount:
                return 1
            
            if summ > amount:
                return 0

            cache[(i,summ)] = dfs(i, summ + coins[i]) + dfs(i+1, summ)

            return cache[(i,summ)]

        return dfs(0,0)