"""
#base cases
if r == ROWS or COLS == COLS: return 0
if r,c == ROWS-1, COLS-1: return 1

Brute Force Recursive way: O(2**n)

Top down memoization: O(m*n)

Bottom up Tabulation: O(m*n) SC: O(1)
  0 1 2  
0[  2,1]
1[1,1,1,1,1,1]


[0,0,0,0,0,1]
[0,0,0,0,0,0]




m * n
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        prevRow = [0] * n

        for r in range(m-1, -1, -1):

            curRow = [0] * n
            curRow[n-1] = 1

            for c in range(n-2, -1, -1):

                curRow[c] = curRow[c+1] + prevRow[c]
                
            prevRow = curRow
        
        return curRow[0]




        