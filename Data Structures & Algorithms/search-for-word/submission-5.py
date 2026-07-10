class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        """
        traverse the matrix
        - if start of the word == board[r][c]:
            - Begin the search
        
        Search Function
        Base Case - out of bounds check, alreayd visited
        Base Case - i == len(word) (out of bound of word)

        - Search all directions - DFS
        - Add the visited positons to a set, so that we know the path we already visited

        """

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        i = 0


        def dfs(r,c,i):

            #basecases
            if i == len(word):
                return True

            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            visited.remove((r,c))
        
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if word[i] == board[r][c]:
                    if dfs(r,c,i):
                        return True
                else:
                    continue
        
        return False