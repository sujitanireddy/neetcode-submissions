"""
- unbounded knapsack
base case: if summ == amount: return 1
           if i >= len(coins): return 0


       0   1   2   3   4
1$  0  1   
2$  1  1
3$  2  1

"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        ROWS = len(coins)
        COLS = amount + 1

        dp = [[0] * COLS for i in range(ROWS)]

        #initialization
        for r in range(ROWS):
            dp[r][0] = 1
        
        for c in range(1,COLS):
            if coins[0] <= c and c % coins[0] == 0:
                dp[0][c] = 1
        
        #true dp 
        for r in range(1, ROWS):
            for c in range(1, COLS):

                if coins[r] > c:
                    dp[r][c] += dp[r-1][c]
                
                else:
                    dp[r][c] = dp[r][c - coins[r]] + dp[r-1][c]
        
        return dp[ROWS-1][COLS-1]








