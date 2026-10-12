"""
3 Conditions:
- if len is bigger then prioritize delete option
- if len is smaller prioritize Insert option
- If len is eqal prioritize Replace option 

Base case?
- if i and j are out of bounds. We can return 0.

"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        cache = {}
        
        def recurse(i,j):

            if (i,j) in cache:
                return cache[(i,j)]

            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                res = recurse(i+1, j+1)
            
            else:
                insert = 1 + recurse(i, j+1)
                delete = 1 + recurse(i+1, j)
                replace = 1 + recurse(i+1, j+1)   
                res = min(insert, delete, replace)
                
            cache[(i,j)] = res
        
            return res

        return recurse(0,0)