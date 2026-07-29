class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(r,c):

            if r < 0 or c < 0 or r == ROWS or c == COLS or ((r,c)) in visit or board[r][c] == "X":
                return

            visit.add((r,c))

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for c in range(COLS):
            dfs(0,c)
            dfs(ROWS-1,c)
        
        for r in range(ROWS):
            dfs(r,0)
            dfs(r,COLS-1)

        print(visit)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and ((r,c)) not in visit:
                    board[r][c] = "X"
        