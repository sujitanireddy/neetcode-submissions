class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(self, array, target):

            L = 0
            R = len(array) - 1

            while L <= R:

                mid = (L + R) // 2

                if array[mid] == target:
                    return True
                
                elif array[mid] > target:
                    R = mid - 1
                
                else:
                    L = mid + 1
            
            return False
        
        L = 0
        R = len(matrix) - 1


        while L <= R:

            mid = (L + R) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:

                return binary_search(self, array=matrix[mid], target=target)
            
            elif matrix[mid][-1] < target:
                L += 1
            
            else:
                R -=1 

        return False
        

