"""
Notes:
- All positive or 0 values

Recursive Tree
dfs(r,c)

TC: O(m*n)
SC: O(m*n)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0

        cache = {}
        
        def dfs(r,c,prev):

            if (r,c,prev) in cache:
                return cache[(r,c,prev)]

            if r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev:
                return 0
            
            cache[(r,c,prev)] = 1 + max(dfs(r+1,c,matrix[r][c]), dfs(r-1,c,matrix[r][c]), dfs(r,c+1,matrix[r][c]),dfs(r,c-1,matrix[r][c]))

            return cache[(r,c,prev)]

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c,-1))
        
        return res
