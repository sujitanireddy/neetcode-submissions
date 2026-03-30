class Solution:
    def search(self, nums: List[int], target: int) -> int:


        def binary_search(arr):
            L = 0
            R = len(arr) - 1

            while L <= R:

                mid = (L + R) // 2

                if arr[mid] == target:
                    return mid
            
                elif arr[mid] > target:
                    R = mid - 1
                
                else:
                    L = mid + 1
            
            return -1


        L = 0
        R = len(nums) - 1 

        min_so_far = float("inf")

        while L <= R:

            mid = (L + R) // 2

            if nums[R] < nums[mid]:

                L = mid + 1 
            
            else:

                min_so_far = min(min_so_far, nums[mid])

                R = mid - 1
        
        partition_point = nums.index(min_so_far)
        
        left_array = binary_search(nums[:partition_point])
        right_array = binary_search(nums[partition_point:])

        print(nums[partition_point:])

        print(right_array)

        if left_array != -1:

            return left_array
        
        elif right_array != -1:

            return len(nums[:partition_point]) + right_array
        
        else:
            return -1 
