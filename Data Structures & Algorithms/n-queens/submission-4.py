class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        """ 

         0 1 2 3
       0 . . . .
       1 . . . .
       2 . . . .
       3 . . . .

        Observations
        - The board is only valid if we place all "n" queens.
        - Matrix. DFS. 
        - sets = cols, posdiag (r+c), negdiag (r-c)
        - within each row in which col can the queen be placed!
        """
        cols = set() 
        posdiag = set()
        negdiag = set()
        res = []
        board = [["."] * n for _ in range(n)]

        print(board)
        
        def backtrack(r):
            #basecases
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for c in range(n):
                if c in cols or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)

        backtrack(0)
        
        return res