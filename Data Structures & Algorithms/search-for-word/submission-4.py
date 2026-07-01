class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        i = 0
        visited = set() #(r,c)

        def dfs(r,c,i):

            #basecases - out of bounds, visited points, not equal char at word
            if i == len(word):
                return True

            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[i] or (r,c) in visited:
                return False
                
            visited.add((r,c))

            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)

            visited.remove((r,c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,i):
                        return True
        
        return False
                


















        