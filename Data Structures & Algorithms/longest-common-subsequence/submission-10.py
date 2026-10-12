"""
            i
c   a   t

                    j
c   r   a   b   t

1
1
1

+1 when matching

if i == len(text1) or j == len(tex2):
    return 0

Conditions:
- If text1[i] == text2[j]:
    recurse(i+1,j+1)
- else:
    - recurse(i, j+1)
    - recurse(i+1,j)

Brute Force recursion:
TC: O(2**n)
SC: O(m*n)

Top down memo:
TC: O(m*n)
SC: O(m*n)

Bottom up DP:

    c   r   a   b    t
c   3   2   2   1    1  0
a   2   2   2   1    1  0
t   1   1   1   1    1  0
    0   0   0   0    0  0


Notes:
- Initiate the dp matrix with 0's
- add extra row and col


"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ROWS = len(text1)
        COLS = len(text2)

        dp = [[0] * (COLS+ 1) for _ in range(ROWS+1)]

        #dp logic 
        for r in range(ROWS-1, -1 ,-1):
            for c in range(COLS-1, -1, -1):

                if text1[r] == text2[c]:
                    dp[r][c] = 1 + dp[r+1][c+1]
                
                else:
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])

        return dp[0][0]







        