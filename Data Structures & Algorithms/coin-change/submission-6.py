"""
                                          1 5 10
                        
                         1                   5                        10

                 2       6      11     6    10     15X         11     15X     20X
        
        3       5     12 (return 1)

base cases:
- if summ == amount: return 1
- if summ > amount:  return 0

BruteForce:
TC: O(2**n)
SC: O(h)

Top Down memoized:
TC: O(n)
SC: O(n)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        ROWS = len(coins)
        COLS = amount + 1
        matrix = [[float("inf")] * COLS for i in range(ROWS)]        

        #Initialize first row: With the first coin can we form the amount(c)?
        for c in range(COLS):
            if c % coins[0] == 0:
                matrix[0][c] = c//coins[0]
        
        #dp logic
        for r in range(1, ROWS):
            for c in range(COLS):

                skip = matrix[r-1][c]

                include = float("inf")

                if c >= coins[r]:
                    include = 1 + matrix[r][c - coins[r]]
                
                matrix[r][c] = min(include, skip)

        print(matrix)
        
        if matrix[ROWS-1][COLS-1] == float("inf"): 
            return -1 
        else:
            return matrix[ROWS-1][COLS-1]



