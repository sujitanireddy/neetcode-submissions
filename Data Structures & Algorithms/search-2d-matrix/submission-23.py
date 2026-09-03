""" 
    L            M              R
    0            1              2
[[1,2,4,8],[10,11,12,13],[14,20,30,40]]

"""



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(arr):
            
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

        
        L = 0 
        R = len(matrix) - 1

        while L <= R:

            mid = (L+R) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binary_search(matrix[mid])
                    
            elif matrix[mid][0] > target:
                R = mid - 1
            
            else:
                L = mid + 1

        return False