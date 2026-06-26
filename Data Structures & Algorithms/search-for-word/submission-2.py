class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        i = 0
        
        def dfs_search(r,c,i):
            
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or word[i] != board[r][c]:
                return False
            
            visited.add((r,c))

            res = dfs_search(r+1, c, i+1) or dfs_search(r-1, c, i+1) or dfs_search(r, c+1, i+1) or dfs_search(r, c-1, i+1)

            visited.remove((r,c))

            return res
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs_search(r,c,i):
                        return True
        
        return False
