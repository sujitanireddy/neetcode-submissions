class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top = left = 0
        right = len(matrix[0])
        bottom = len(matrix)
        res = []

        while left < right and top < bottom:

            for i in range(left, right):
                res.append(matrix[top][i])
            
            for i in range(top + 1, bottom):
                res.append(matrix[i][right - 1])
            
            if right - left == 1 or bottom - top == 1:
                break

            for i in range(right - 2, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            
            for i in range(bottom - 2, top, -1):
                res.append(matrix[i][left])
            
            top += 1
            left += 1
            right -= 1
            bottom -= 1
        
        return res

