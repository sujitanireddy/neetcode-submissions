class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr):
            
            L = 0
            R = len(arr) - 1 

            print(arr)

            while L <= R:

                mid_point = (L + R) // 2

                if target == arr[mid_point]:
                    return True
                    
                elif target > arr[mid_point]:
                    L = mid_point + 1
                    
                else:
                    R = mid_point - 1
            
            return False
        
        L = 0 
        R = len(matrix) - 1

        while L <= R:

            mid = (L + R) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binary_search(matrix[mid])

            elif matrix[mid][-1] < target:
                L = mid + 1 
            
            else:
                R = mid - 1
        
        return False

