"""

    L       R
    1   2   3
T   3   5   6
B   4   7   9

"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        res = []

        while left < right and top < bottom:

            #walk top col
            for c in range(left, right):
                res.append(matrix[top][c])
            top += 1

            #walk the last row
            for r in range(top, bottom):
                res.append(matrix[r][right - 1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            #walk the bottom col
            for c in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][c])
            bottom -= 1

            #walk to first row
            for r in range(bottom - 1, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
        
        return res