class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        mark_rows = [False] * ROWS
        mark_cols = [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    mark_rows[r] = True
                    mark_cols[c] = True
        
        for r in range(ROWS):
            for c in range(COLS):
                if mark_rows[r] or mark_cols[c]:
                    matrix[r][c] = 0
        