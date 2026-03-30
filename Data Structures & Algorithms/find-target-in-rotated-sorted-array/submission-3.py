class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(array):

            L = 0
            R = len(array) - 1

            while L <= R:

                mid = (L+R) // 2

                if array[mid] == target:
                    return mid

                elif array[mid] > target:
                    R = mid - 1

                else:
                    L = mid + 1
            
            return -1 
        
        L = 0 
        R = len(nums) - 1

        while L < R:

            mid = (L+R) // 2

            if nums[mid] > nums[R]:

                L = mid + 1
            
            elif nums[mid] < nums[R]:

                R = mid
        
        pivot = R

        target_idx_found_left = binary_search(nums[:pivot])
        target_idx_found_right = binary_search(nums[pivot:])


        if target_idx_found_left != -1:
            return target_idx_found_left
        
        elif target_idx_found_right != -1:
            return len(nums[:pivot]) + target_idx_found_right
        
        else:
            return -1 


        
        