class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        """
        Binary Search - O(log n)
        Binary Search on the array to compare if the target exisits within that range if it done then binary search again on that array
        """

        def binary_search(arr):

            L = 0
            R = len(arr) - 1

            while L <= R:

                mid = (L + R) // 2

                if arr[mid] == target:
                    return True
                
                elif arr[mid] > target:
                    R = mid - 1
                
                else:
                    L = mid + 1
            
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