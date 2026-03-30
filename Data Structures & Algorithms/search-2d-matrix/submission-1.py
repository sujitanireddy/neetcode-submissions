class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        matrix_list = []

        l, r = 0, len(matrix) - 1

        while l <= r:
           
            m = (l + r) // 2

            if matrix[m][0] <= target <= matrix[m][-1]:
                matrix_list = matrix[m]
                break
            
            elif matrix[m][-1] < target:
                l = m + 1
            
            else:
                r = m - 1 

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