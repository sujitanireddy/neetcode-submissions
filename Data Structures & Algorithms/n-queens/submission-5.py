class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        """
         0 1 2 3
      0  . . . .
      1  . . . .
      2  . . . .
      3  . . . .

        posdiag = (r + c)
        negdiag = (r - c)

        dfs(r):
        - basecases
        - r == n
        """

        posdiag = set()
        negdiag = set()
        cols = set()
        board = [["."] * n for _ in range(n)]
        res = []

        def dfs(r,c):

            if r == n:
                copy = ["".join(row) for row in board]
                print(copy)
                res.append(copy)
                return 
        
            for c in range(n):

                if (r-c) in negdiag or (r+c) in posdiag or c in cols:
                    continue
                
                else:
                
                    board[r][c] = "Q"
                    posdiag.add((r+c))
                    negdiag.add((r-c))
                    cols.add(c)

                    dfs(r+1, c)

                    board[r][c] = "."
                    posdiag.remove((r+c))
                    negdiag.remove((r-c))
                    cols.remove(c)


        dfs(0,0)

        return res