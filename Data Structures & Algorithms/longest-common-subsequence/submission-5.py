"""
i 
c   a   t

j
c   r   a   b   t


- while iterating through text1 and text2
    - if match = add one and incrment both i and j
    - if no match - we have two options
        - recursivly go depper into both those options 


Base case? 
- if eiter i, j go out of bounds

"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}
        
        def recurse(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if i >= len(text1) or j >= len(text2):
                return 0

            res = float("-inf")
            
            if text1[i] == text2[j]:
                res = 1 + recurse(i+1, j+1)
            
            else:
                res = max(res, recurse(i, j+1), recurse(i+1, j))
                cache[(i,j)] = res
        
            return res


        return recurse(0,0)