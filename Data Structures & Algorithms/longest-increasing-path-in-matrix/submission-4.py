"""
BruteForce DFS on every cell in matrix while keeping track of longest increasing path so far

TC: O(4**(m*n)
SC: O(m*n)


"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0
        cache = {}

        def dfs(r,c,prev):

            if r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev:
                return 0

            if (r,c) in cache:
                return cache[(r,c)]

            res = 1 + max(dfs(r+1,c,matrix[r][c]), dfs(r,c+1,matrix[r][c]), dfs(r-1,c,matrix[r][c]), dfs(r,c-1,matrix[r][c]))

            cache[(r,c)] = res

            return res


        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c,float("-inf")))
        
        return res
        