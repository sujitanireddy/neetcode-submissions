class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ROWS = len(coins)
        COLS = amount + 1

        matrix = [[float("inf")] * COLS for i in range(ROWS)]

        #initalize my first row
        for c in range(COLS):
            if c % coins[0] == 0:
                matrix[0][c] = c // coins[0]

        #core dp logic
        for r in range(1,ROWS):
            for c in range(COLS):
                
                skip = matrix[r-1][c]
                
                include = float("inf")
                
                #Can we include?
                if c >= coins[r]:
                    include = 1 + matrix[r][c - coins[r]]
                
                matrix[r][c] = min(skip, include)
            
        res = matrix[ROWS-1][COLS-1]

        return -1 if res == float("inf") else res


    
