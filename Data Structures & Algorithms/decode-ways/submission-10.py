"""
Notes:
- if 0 comes first then that's invalid
- Can I decode the entire string choosing 1 char?

        i            
            j          
1   0   1   2

A   B   A   F       1 Way
  L     A   F
  L     )

for two digits the number should be 10 <= num >= 26

Base case: 
- if i >= len(s) and j >= len(s):
    return 1

dfs(i+1, j+1)
dfs(i, j+1)

"""
class Solution:
    def numDecodings(self, s: str) -> int:

        cache = {}
        
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]

            if s[i:j+1] == "0":
                return 0
            
            if i >= len(s) and j >= len(s):
                return 1
            
            two_char_decode = 0
            
            single_char_decode = dfs(i+1,j+1)

            if 10 <= int(s[i:j+2]) <= 26 and i < len(s) - 1:
                two_char_decode = dfs(i+2, j+2)
            
            cache[(i,j)] = single_char_decode + two_char_decode

            return cache[(i,j)]

















        return dfs(0,0)
