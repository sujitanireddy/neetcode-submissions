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

        ROWS = len(text1) + 1
        COLS = len(text2) + 1

        #Build the matrix
        matrix = [[0] * COLS for r in range(ROWS)]

        #dp logic
        for r in range(1, ROWS):
            for c in range(1, COLS):

                if text1[r-1] == text2[c-1]:
                    matrix[r][c] = matrix[r-1][c-1] + 1
                
                else:
                    matrix[r][c] += max(matrix[r-1][c], matrix[r][c-1])
        
        return matrix[ROWS-1][COLS-1]