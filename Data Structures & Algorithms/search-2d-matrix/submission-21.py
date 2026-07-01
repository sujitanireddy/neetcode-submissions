class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        """
        target = 10
            L            M             R
        [[1,2,4,8],[10,11,12,13],[14,20,30,40]]

        """

        def binary_search(arr):

            L = 0
            R = len(arr) - 1

            while L <= R:

                mid_p = (L + R) // 2

                if arr[mid_p] == target:
                    return True
                
                elif arr[mid_p] > target:
                    R = mid_p - 1
                
                else:
                    L = mid_p + 1
            
            return False


        """
        matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target=3
        """




        L = 0
        R = len(matrix) - 1

        while L <= R:
            
            mid = (L + R) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                if binary_search(matrix[mid]):
                    return True
                else:
                    return False
            
            elif matrix[mid][0] > target:
                R = mid - 1
            
            else:
                L = mid + 1
        
        return False