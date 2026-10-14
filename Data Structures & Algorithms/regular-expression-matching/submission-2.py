"""
if s[i] == char and p[j] == "." then increment both i and j pointers
if s[i] == p[j]: (i+1, j+1)
if s[i] == char and p[j] == "*":
    if p[j-1] == s[i]: (i+1, j)
    elif p[j-1] == ".": (i+1, j+1) and j is not end of string
        return False

- if * is at the end of the string, we can keep choosing


- if i goes out of bounds then we can return True
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        cache = {}

        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]

            if i >= len(s) and j >= len(p):
                return True
            
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j+1] == "*":
                skip_star = dfs(i, j+2)
                choose_star = match and dfs(i+1, j)
                cache[(i,j)] = skip_star or choose_star
                return cache[(i,j)]
            
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]

            cache[(i,j)] = False
            return False
    
        return dfs(0,0)