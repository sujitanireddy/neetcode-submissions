class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDiag = set() #marks pos diags (r+c)
        negDiag = set() #marks neg diags (r-c)
        cols = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def dfs(r):

            if r == n:
                copy_of_board = ["".join(row) for row in board]
                res.append(copy_of_board)
                return
            
            for c in range(n):

                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                dfs(r+1)

                board[r][c] = "."
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

        dfs(0)
        return res