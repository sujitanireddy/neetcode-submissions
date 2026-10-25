"""
            i
c   a   t

                    j
c   r   a   b   t


                i   
a   b   c   d

j   
e   f   g   h

Base cases:

if i >= len(text1) or j >= len(text2):
    return 0

if text1[i] == text2[j]:
    dfs(i+1, j+1) + 1

else:
    dfs(i+1, j)
    dfs(i, j+1)

"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}
        
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if i >= len(text1) or j >= len(text2):
                return 0

            match = skip_text1 = skip_text2 = float("-inf")
            
            if text1[i] == text2[j]:
                match = dfs(i+1, j+1) + 1
            
            else:
                skip_text1 = dfs(i+1, j)
                skip_text2 = dfs(i, j+1)
            
            cache[(i,j)] =  max(match, skip_text1, skip_text2)

            return cache[(i,j)]

        return dfs(0,0)