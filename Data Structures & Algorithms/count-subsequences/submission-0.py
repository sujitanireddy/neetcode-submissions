"""
- if we reach the end of the s string all possible subsequences are done. Go to next one



"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        if len(s) < len(t):
            return 0

        cache = {}
        
        def recurse(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0

            choose, skip = 0,0 
            
            #choose
            if s[i] == t[j]:
                choose = recurse(i+1,j+1)
            
            skip = recurse(i+1, j)

            cache[(i,j)] = choose + skip

            return choose + skip

        return recurse(0,0)