"""
[1,2,3]

- Recursive sol (unbounded knapsack)

Base Cases:
- out of bounds check
- target hit check
- summ over target hit

DP matrix (dry run)

        0   1   2   3   4
1   0   1   1   1   1   1
2   1   1   1   2   2   3
3   2   1   1   2   3   4


First row initialization:
- if c >= coins[i] and c % coins[i] == 0:
    dp[0][c] = (c // coins[i])



"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        ROWS = len(coins)
        COLS = amount + 1

        dp = [[0] * (COLS) for _ in range(ROWS)]

        #First col initialization
        for c in range(1, COLS):
            if c >= coins[0] and c % coins[0] == 0:
                dp[0][c] = 1
        
        #First row initialization
        for r in range(ROWS):
            dp[r][0] = 1
            
        #dp logic
        for r in range(1, ROWS):
            for c in range(1, COLS):

                if coins[r] > c:
                    dp[r][c] += dp[r-1][c]
                
                else:
                    dp[r][c] = dp[r][c-coins[r]] + dp[r-1][c]
        
        return dp[ROWS-1][COLS-1]
                

