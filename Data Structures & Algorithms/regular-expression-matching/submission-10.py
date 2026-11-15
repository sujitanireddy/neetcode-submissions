"""
    i   
a

 j
a * b


Conditions:

- if both i and j go out of bounds: return True
- if j goes out of bounds return False

match = i < len(s) and (s[i] == p[j] or p[j] == ".")

if j < len(p) - 1 and p[j+1] == "*":
    if match:
        dfs(i+1, j)
    dfs(i, j+2)

if match:
    dfs(i+1, j+1)

i
x   y   z

j
.   *   z

i
a   a   b

        j
c   *   a   *   b

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

            star_matched = star_empty = matched = False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j < len(p) - 1 and p[j+1] == "*":
                
                if match:
                    star_matched = dfs(i+1, j)
                
                star_empty = dfs(i, j+2)
            
            if match:
                matched = dfs(i+1, j+1)

            cache[(i,j)] = star_matched or star_empty or matched

            return cache[(i,j)]

        return dfs(0,0)






































