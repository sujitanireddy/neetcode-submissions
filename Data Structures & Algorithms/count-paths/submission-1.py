"""
#base cases
if r == ROWS or COLS == COLS: return 0
if r,c == ROWS-1, COLS-1: return 1

Brute Force Recursive way: O(2**n)

Top down memoization: O(m*n)

Bottom up Tabulation: O(m*n) SC: O(1)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = {}

        def recurse(r,c):

            if (r,c) in cache:
                return cache[(r,c)]

            if r == m or c == n:
                return 0
            
            if r == m-1 and c == n-1:
                return 1
            
            cache[(r,c)] = recurse(r+1,c) + recurse(r,c+1)

            return cache[(r,c)]
        
        return recurse(0,0)