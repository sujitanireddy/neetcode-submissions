"""
Notes:

                        i
0   1   2   3   4   5   6                 
m   o   n   k   e   l   s   

                        j
0   1   2   3   4   5   6
m   o   n   k   e   y   s 

Matches:
if word1[i] == word2[j]:
    dfs(i+1, j+1)
else:
- Insert : (i, j+1) + 1
- Delete : (i+1, j) + 1
- Replace : (i+1, j+1) + 1

#base case
if j >= len(word2):
    return len(word1) - i

if i >= len(word1):
    return len(word2) - j
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = {}
        
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if j >= len(word2):
                return len(word1) - i

            if i >= len(word1):
                return len(word2) - j

            match = replace = insert = delete = float("inf")
            
            if word1[i] == word2[j]:
                match = dfs(i+1, j+1)

            else:
                replace = dfs(i+1, j+1) + 1
                insert = dfs(i, j+1) + 1
                delete = dfs(i+1, j) + 1

            cache[(i,j)] = min(match, replace, insert, delete)

            return cache[(i,j)] 

        return dfs(0,0)