class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for arr in matrix:

            if arr[0] <= target <= arr[-1]:
                
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
