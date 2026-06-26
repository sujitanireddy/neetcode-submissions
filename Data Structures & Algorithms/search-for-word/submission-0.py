class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()
        i = 0 

        def dfs(r,c,i):

            #base case
            if i == len(word):
                return True
            
            #out of bound check, if word is not matching check and path already visited check
            if min(r,c) < 0 or ROWS == r or COLS == c or word[i] != board[r][c] or (r,c) in seen:
                return False
            
            seen.add((r,c))

            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)

            seen.remove((r,c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,i):
                    return True
        
        return False






