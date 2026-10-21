"""
s3 pointer can be derived by addding i and j




"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        cache = {}
        
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]

            if i >= len(s1) and j >= len(s2) and (i + j) >= len(s3):
                return True

            if (i + j) >= len(s3):
                return False
            
            res1 = res2 = False
            
            if i < len(s1) and s1[i] == s3[i+j]:
                res1 = dfs(i+1, j)
            
            if j < len(s2) and s2[j] == s3[i+j]:
                res2 = dfs(i, j+1)

            cache[(i,j)] = res1 or res2

            return cache[(i,j)]

        return dfs(0,0)
