"""
  0 1 2 3
0 Q . . .
1 . . . .
2 . . . .
3 . . . .

negDiag = r - c
posDIag = r + c

visit(0,0)

[['.''.''.''.']...]
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        negDiag = set()
        posDiag = set()
        cols = set()

        board = [['.'] * n for i in range(n)]
        res = []


        def backtrack(r):
            
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):

                if c in cols or (r+c) in posDiag or (r-c) in negDiag:
                    continue
                
                board[r][c] = 'Q'
                cols.add(c)
                negDiag.add((r-c))
                posDiag.add((r+c))

                backtrack(r+1)

                board[r][c] = '.'
                cols.remove(c)
                negDiag.remove((r-c))
                posDiag.remove((r+c))


        backtrack(0)

        return res