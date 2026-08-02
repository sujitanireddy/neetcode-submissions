class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
          0 1 2 3
        0 . . . .
        1 . . . .
        2 . . . .
        3 . . . .

        negdiag = (r-c)
        posdiag = (r+c)
        """
        cols = set()
        rows = set()
        posdiag = set()
        negdiag = set()
        board = [["."] * n for _ in range(n)]
        res = []

        def dfs(r):
            
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):

                if r < 0 or c < 0 or r == n or c == n or c in cols or r in rows or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                rows.add(r)
                posdiag.add(r+c)
                negdiag.add(r-c)

                dfs(r+1)

                board[r][c] = "."
                cols.remove(c)
                rows.remove(r)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        

        dfs(0)
        return res








