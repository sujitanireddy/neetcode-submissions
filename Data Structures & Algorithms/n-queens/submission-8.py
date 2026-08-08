class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        """
          0 1 2 3
        0[
          [Q . . .]
        1 [. . . .]
        2 [. . . .]
        3 [. . . .]
        4
         ]

        posDiag = (r+c)
        negDiag = (r-c)

        While backtracking, remove from visit sets and replace the Q's with "."
        4m*n
        """
        posDiag = set()
        negDiag = set()
        cols = set()

        board = [["."] * n for i in range(n)]
        res = []

        print(board)

        def backtrack(r):
            
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):

                if r+c in posDiag or r-c in negDiag or c in cols:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                negDiag.add(r-c)
                posDiag.add(r+c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                negDiag.remove(r-c)
                posDiag.remove(r+c)


        backtrack(0)
        return res