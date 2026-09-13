"""
     0 1 2 3 4 5 6 7 8 9 10 11 12
1  0 0 1 2 3 4 5 6 7 8 9 10 11 12  
5  1 0 1 2 3 4 1 . . . .  .  .  . 
10 2 . . . . . . . . . .  .  .  . 

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        ROWS = len(coins)
        COLS = amount + 1

        matrix = [[float("inf")] * COLS for r in range(ROWS)]

        #initialize the first row
        for c in range(COLS):
            if c % coins[0] == 0:
                matrix[0][c] = (c // coins[0])
        
        #dp logic
        for r in range(1, ROWS):
            for c in range(COLS):

                include = float("inf")

                skip = matrix[r-1][c]

                if (c - coins[r]) >= 0:
                    include = 1 + matrix[r][c - coins[r]]
                
                matrix[r][c] = min(skip, include)
        
        res = matrix[ROWS-1][COLS-1] 

        return res if res != float("inf") else -1

                
