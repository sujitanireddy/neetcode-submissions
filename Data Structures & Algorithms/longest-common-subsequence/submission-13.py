"""
            i
c   a   t

                    j
c   r   a   b   t


                i   
a   b   c   d

j   
e   f   g   h

Base cases:

if i >= len(text1) or j >= len(text2):
    return 0

if text1[i] == text2[j]:
    dfs(i+1, j+1) + 1

else:
    dfs(i+1, j)
    dfs(i, j+1)


        0   1   2   3   4   5
        c   r   a   b   t   -
0   c   3   2   2   1   1   0
1   a   2   2   2   1   1   0
2   t   1   1   1   1   1   0       new_dp
3   -   0   0   0   0   0   0       dp

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [0] * (len(text2) + 1)

        for r in range(len(text1) - 1, -1 ,-1):

            new_dp = [0] * (len(text2) + 1)

            for c in range(len(text2) - 1, -1, -1):

                if text1[r] == text2[c]:
                    new_dp[c] = dp[c+1] + 1
                
                else:
                    new_dp[c] = max(dp[c], new_dp[c+1])
            
            dp = new_dp
        
        return dp[0]

            














