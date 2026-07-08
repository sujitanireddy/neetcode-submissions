class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        """
          0 1 2 3
        0 Q . . . 
        1 . . . .
        2 . . . .
        3 . . . .

        Only validate cols and diagnals. 
        Increment row by one every single time 
        Recursivly DFS and backtrack

        [['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
        """

        cols = set()
        posdiag = set()
        negdiag = set()
        board = [["."] * n for _ in range(n)]
        res = []


        def backtrack(r):

            #basecases
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                
                if c in cols or (r + c) in posdiag or (r - c) in negdiag:
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

        