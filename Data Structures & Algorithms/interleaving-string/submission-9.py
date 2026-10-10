"""
Early return:
- if len(s1) + len(s2) != len(s3): return False

Base case:
- If we go out of bounds with both s1, s2 and s3 strings then we can return true 
- if either j or i is out of bounds then don't consider that branch.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3): 
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True

        for r in range(len(s1), -1, -1):
            for c in range(len(s2), -1, -1):

                if r < len(s1) and s1[r] == s3[r+c] and dp[r+1][c]:
                    dp[r][c] = True
                
                if c < len(s2) and s2[c] == s3[r+c] and dp[r][c+1]:
                    dp[r][c] = True
        
        return dp[0][0]
