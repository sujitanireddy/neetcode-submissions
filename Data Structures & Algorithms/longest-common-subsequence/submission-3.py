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
      
      c r a b t
    0 1 2 3 4 5
  0 0 0 0 0 0 0  
c 1 0 0 0 0 0 0 
a 2 0 0 0 0 0 0 
t 3 0 0 0 0 0 0 

"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2) 

        matrix = [[0] * (m + 1) for i in range(n+1)]

        print(matrix)

        for i in range(n):
            for j in range(m):

                if text1[j] == text2[i]:
                    matrix[i+1][j+1] = 1 + matrix[i][j]
                
                else:
                    matrix[i+1][j+1] = max(matrix[i+1][j], matrix[i][j+1])
        
        return matrix[n][m]




































