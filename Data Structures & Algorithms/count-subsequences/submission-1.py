"""

                i
c   a   a   a   t  

        j
c   a   t


                    i
x   x   y   x   y

    j
x   y

Notes:
- we always have to keep the relative order of chars
- if j go out of bounds we found a valid subsequence
- if i goes out of bounds wihtout j then we can return 0

"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(t) > len(s):
            return 0
        
        cache = {}
        
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if j >= len(t):
                return 1

            if i >= len(s):
                return 0
            
            match, no_match = 0,0
            
            if s[i] == t[j]:
                match = dfs(i+1, j+1)
            
            no_match = dfs(i+1, j)

            cache[(i,j)] = match + no_match

            return cache[(i,j)]

        return dfs(0,0)

