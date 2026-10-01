"""
Recursion
 
   i
[1,5,10]                                 start of recursion

                                   [1]                         []

                          [1,1]             [1]             [5]           []
                        
                   [1,1,1]              [1,5]   [1]    [1]     [5,5]   [5] ....

            [1,1,1,1]   [1,1,1]    [1,5,10]        

Base Case:
- if summ == amount:
        return 0

True Dp solution:

        0 1 2 3 4 5 6 7 8 9 10 11 12
1    0  0 1 2 3 4 5 6 7 8 9 10 11 12
2    1  0 1 1  
3    2

"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #build the matrix
        ROWS = len(coins)
        COLS = amount + 1
        matrix = [[float("inf")] * COLS for i in range(ROWS)]

        #initilizing the first row
        for c in range(COLS):
            if c % coins[0] == 0:
                matrix[0][c] = c // coins[0]
        
        #unbounded knapsack dp logic
        for r in range(1,ROWS):
            for c in range(COLS):

                include = float("inf")

                skip = matrix[r-1][c]

                if c >= coins[r]:
                    include = 1 + matrix[r][c - coins[r]]
                
                matrix[r][c] = min(skip, include)

        res = matrix[ROWS-1][COLS-1]
        
        if res == float("inf"):
            return -1
        else:
            return res 




