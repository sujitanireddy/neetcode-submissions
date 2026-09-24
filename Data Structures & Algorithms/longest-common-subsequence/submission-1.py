"""

        i
0   1   2
c   a   t

                j
0   1   2   3   4
c   r   a   b   t

                                                (0,0)
                                                  |
                                                (1,1)
    
                                            (1,2)       (2,1)

                                            (2,3)

                                        x(3,3) (2,4)

                                               X(3,4)

Recursive Way:

Base case:
- if i == len(text1) or j == len(text2):
    return 0

- if text1[i] == text2[j]: 
    return 1 + recurse(i+1, j+1)

- if not matching
    return max(recurse(i, j+1), recurse(i+1, j))

"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache = {}
        
        def recurse(i,j):

            if (i,j) in cache:
                return cache[(i,j)]
            
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                return 1 + recurse(i+1,j+1)

            cache[(i,j)] = max(recurse(i,j+1), recurse(i+1,j))

            return cache[(i,j)]

        return recurse(0,0)



































