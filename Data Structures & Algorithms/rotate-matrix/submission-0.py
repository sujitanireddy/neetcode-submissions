"""
      L        R  
      0  1  2  3 
T 0   1, 2, 3, 11
  1   4, 5, 6, 12
  2   7, 8, 9, 13
B 3   14,15,16,17


"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        top, bottom = 0, len(matrix) - 1
        
        while top < bottom:

            left, right = top, bottom

            for i in range(bottom - top):
                
                #save top_left
                top_left = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left]

                matrix[bottom - i][left] = matrix[bottom][right - i]

                matrix[bottom][right - i] = matrix[top + i][right]

                matrix[top + i][right] = top_left

            top += 1
            bottom -= 1 