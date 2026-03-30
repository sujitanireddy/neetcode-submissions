class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(mid_array):

            L = 0
            R = len(mid_array) - 1

            while L <= R:

                mid = (L+R) // 2

                if mid_array[mid] == target:
                    return True

                elif mid_array[mid] < target:
                    L = mid + 1
                
                else:
                    R = mid - 1
            
            return False

        L = 0
        R = len(matrix) - 1

        while L <= R:

            mid = (L + R) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binary_search(matrix[mid])
            
            elif matrix[mid][0] > target:
                R = mid - 1
            
            else:
                L = mid + 1

        return False