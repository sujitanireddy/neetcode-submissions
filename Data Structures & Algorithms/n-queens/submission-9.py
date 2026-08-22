"""
4
  0 1 2 3 
0 . . . .
1 . . . .
2 . . . .
3 . . . .

- correct pos in the row
- posdiag, negdiag, cols

iterate over the cols

if i == n: we found a valid board

"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [["."] * n for i in range(n)]
        res = []
        posDiag = set() #(r+c)
        negDiag = set() #(r-c)
        cols = set()

        def backtrack(r):
            
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):

                if c in cols or r+c in posDiag or r-c in negDiag:
                    continue
                
                board[r][c] = "Q"
                posDiag.add(r+c)
                negDiag.add(r-c)
                cols.add(c)

                backtrack(r+1)

                board[r][c] = "."
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                cols.remove(c)


        backtrack(0)

        return res

