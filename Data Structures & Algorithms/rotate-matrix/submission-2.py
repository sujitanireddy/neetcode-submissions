class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        top, bottom = 0, len(matrix) - 1

        while top < bottom:

            for i in range(bottom - top):

                left, right = top, bottom

                #save top left value
                top_left = matrix[top][left + i]

                matrix[top][left + i] = matrix[bottom - i][left]

                matrix[bottom - i][left] = matrix[bottom][right - i]

                matrix[bottom][right - i] = matrix[top + i][right]

                matrix[top + i][right] = top_left
            
            top += 1
            bottom -= 1