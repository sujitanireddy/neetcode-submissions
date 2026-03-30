class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrix_list = []

        for m_row in matrix:
            for value in m_row:
                matrix_list.append(value)
        
        left, right = 0, len(matrix_list) - 1

        while left <= right:

            mid = (left + right) // 2

            if matrix_list[mid] == target:
                return True

            elif matrix_list[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return False
            
            
            
        