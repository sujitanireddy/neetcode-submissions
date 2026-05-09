class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr):
            
            L = 0
            R = len(arr) - 1
            
            while L <= R:

                mid = (L + R) // 2

                if arr[mid] == target:
                    return True
                
                elif target > arr[mid]:
                    L = mid + 1
                
                else:
                    R = mid - 1 
            
            return False

        L = 0 
        R = len(matrix) - 1

        while L <= R:

            mid = (L + R) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if binary_search(matrix[mid]):
                    return True
                else:
                    return False
            
            elif target > matrix[mid][-1]:
                L = mid + 1
            
            else:
                R = mid - 1

        return False
        