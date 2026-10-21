class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        ROWS = len(word1)
        COLS = len(word2)

        dp = [[0] * (COLS+1) for _ in range(ROWS+1)]

        #Initialization
        for r in range(ROWS+1):
            dp[r][COLS] = ROWS - r
        
        for c in range(COLS+1):
            dp[ROWS][c] = COLS - c

        #true dp
        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):

                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]
            
                else:
                    dp[r][c] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1])
        
        return dp[0][0]