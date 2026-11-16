class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        longest_path = 0
        cache = {}

        def dfs(r,c,prev):
            
            if r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev:
                return 0

            if (r,c) in cache:
                return cache[(r,c)]

            prev = matrix[r][c]

            cache[(r,c)] = 1 + max(dfs(r+1, c, prev), dfs(r-1, c, prev), dfs(r, c+1, prev), dfs(r, c-1, prev))

            return cache[(r,c)]

        for r in range(ROWS):
            for c in range(COLS):
                longest_path = max(longest_path, dfs(r,c,float("-inf")))

        return longest_path



        