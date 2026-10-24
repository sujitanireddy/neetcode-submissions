"""

(((*)

Base cases:

- if i >= len(s):
    return True

- if open > (len(s) - i):
    return False

- if close > open:
    return False

dfs(i, openn, close)
"""
class Solution:
    def checkValidString(self, s: str) -> bool:

        cache = {}
        
        def dfs(i, openn, close):

            if (i,openn, close) in cache:
                return cache[(i,openn,close)]

            if i >= len(s) and openn != close:
                return False

            if i >= len(s) and openn == close:
                return True

            if close > openn:
                return False
            
            open_para = close_para = skip = star_open = star_close = False
            
            if s[i] == "(":
                open_para = dfs(i+1, openn+1, close)

            elif s[i] == ")":
                close_para = dfs(i+1, openn, close+1)

            else:
                skip = dfs(i+1, openn, close)
                star_open = dfs(i+1, openn+1, close)
                star_close = dfs(i+1, openn, close+1)

            cache[(i,openn,close)] = open_para or close_para or skip or star_open or star_close

            return cache[(i,openn,close)]

        return dfs(0,0,0)