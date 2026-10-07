""" 
 0 1 2 3 4
[1,3,4,0,4]
                                        0
                                    1       0
                                2       0
                            2       2
                        
                        6

two recursive branches
- cooldown
- buy or sell
    buy = dfs() - prices[i]
    sell = dfs() + prices[i]

TC: O(n)
SC: O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cache = {}
        
        def dfs(i, buy):

            if (i,buy) in cache:
                return cache[(i,buy)]
            
            if i >= len(prices):
                return 0
            
            #cooldown
            cooldown = dfs(i+1, buy)

            #buy or sell
            if buy:
                res = max(dfs(i+1, False) - prices[i], cooldown)
            else:
                res = max(dfs(i+2, True) + prices[i], cooldown)

            cache[i,buy] = res

            return res


        return dfs(0, True)