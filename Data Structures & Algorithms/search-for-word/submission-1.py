class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        i = 0

        def dfs(r,c,i):

            if i == len(word):
                return True
            
            if r < 0 or c < 0 or ROWS == r or COLS == c or ((r,c) in path) or word[i] != board[r][c]:
                return False
            
            path.add((r,c))

            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)

            path.remove((r,c))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,i):
                    return True
        
        return False