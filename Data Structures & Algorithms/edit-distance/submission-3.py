"""
            i
0   1   2   3   4   5   6
m   o   n   k   e   y   s

            j
0   1   3   4   5
m   o   n   e   y   

            i
n   e   a   t   c   d   e   e

            j
n   e   e   t   c   o   d   e

    i
m   a   d
    j
m   d

        i
l   a   d

            j
l   a   a   d


Notes:
- If j or i goes out of bounds we are done: return 0
- delete is dfs(i+1,j)
- replace is dfs(i+1, j+1)
- Insert is dfs(i+1, j)


"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = {}
        
        def dfs(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if i == len(word1):
                return len(word2) - j
            
            if j == len(word2):
                return len(word1) - i

            match = insert = delete = replace = float("inf")
            
            if word1[i] == word2[j]:
                match = dfs(i+1, j+1)
            
            else:
                insert = 1 + dfs(i, j+1)
                delete = 1 + dfs(i+1, j)
                replace = 1 + dfs(i+1, j+1)
        
            cache[(i,j)] =  min(match, insert, delete, replace)

            return cache[(i,j)]

        return dfs(0,0)






























