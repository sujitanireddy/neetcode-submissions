"""
            
0   1  2     
c  

                j
0   1   2   3   4
c   r   a   b   t

base case:
if i >= len(text1) or j >= len(text2):
    return 0

conditions:

if text1[i] == text2[j]:
    1 + dfs(i+1, j+1)

dfs(i, j+1)
dfs(i+1, j)


"""



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}
        
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if i >= len(text1) or j >= len(text2):
                return 0

            match = increment_i = increment_j = float("-inf")
            
            if text1[i] == text2[j]:
                match = 1 + dfs(i+1, j+1)

            increment_j = dfs(i, j+1)
            increment_i = dfs(i+1, j)

            cache[(i,j)] = max(match, increment_i, increment_j)

            return cache[(i,j)]
   
        return dfs(0,0)