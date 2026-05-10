class Solution:
    
    def binary_search(self, arr, target):

        L = 0 
        R = len(arr) - 1

        while L <= R:

            mid = (L+R) // 2

            if arr[mid] == target:
                return True
            
            elif target > arr[mid]:
                L = mid + 1
            
            else:
                R = mid - 1
        
        return False
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        L = 0 
        R = len(matrix) - 1

        while L <= R:

            mid = (L+R) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if self.binary_search(matrix[mid], target):
                    return True
                else:
                    return False
            
            elif target > matrix[mid][-1]:
                L = mid + 1 
            
            else:
                R = mid - 1

        return False