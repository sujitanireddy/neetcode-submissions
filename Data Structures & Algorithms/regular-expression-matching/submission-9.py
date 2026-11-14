"""
s = a   a

p = .  b



i
a   a

j
.   b


example 2:

            i
n   n   n

j
n   *


i
x   y   z

j
.   *   z

conditions? 

if i goes out of bounds: return True

match = True if s[i] == p[j] else False

while p[j+1] == "*" and (match or p[j] == "."):
    dfs(i+1, j)

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

            star_matched = matched = star_matched_skipped = False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j < len(p) - 1 and p[j+1] == "*":

                if match:
                    star_matched = dfs(i+1, j)
                
                star_matched_skipped = dfs(i, j+2)
            
            if match:
                matched = dfs(i+1, j+1)
            
            cache[(i,j)] = star_matched or matched or star_matched_skipped

            return cache[(i,j)]

        return dfs(0,0)



























        