"""
s = "aa", p = "ab"

s = "nnn", p = "nnn"

s = "xyz", p = "xyz"

    i
a   b   c

    j
a

* = we can either skip or choose unlimited

            i
n   n   n

j
n*

Base Case:
- if i goes out of bounds: return True
- if j goes out of bounds: return False

if [j+1] == "*":
    (i+1, j)

if p[j] == ".":
    (i+1, j+1)

if s[i] == p[j]:
    (i+1, j+1)

                            i
e   l   e   m   e   n   t

    j
e   .   *   m   e   .   *

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

            skip_star = choose_star = matched = no_match = False

            match = i < len(s) and (p[j] == s[i] or p[j] == ".")

            #encoutering a star
            if j < len(p) - 1 and p[j+1] == "*":
                skip_star = dfs(i, j+2)
                choose_star = match and dfs(i+1, j)
            
            if match:
                matched = dfs(i+1, j+1)
                
            cache[(i,j)] = skip_star or choose_star or matched or no_match

            return cache[(i,j)]

        return dfs(0,0)

        





































        