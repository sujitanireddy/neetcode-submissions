"""

"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = {}
        
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]

            if j >= len(t):
                return 1
            
            if i >= len(s):
                return 0
            
            match = 0
            
            if s[i] == t[j]:
                match = dfs(i+1, j+1)
            
            no_match = dfs(i+1, j)

            cache[(i,j)] = match + no_match

            return cache[(i,j)]
        
        return dfs(0,0)
