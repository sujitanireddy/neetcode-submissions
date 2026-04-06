class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Algorithm
        #Binary search for the min in rotated sorted array.
        #Slice the array into two sub arrays and binary search them.

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

        while L < R:

            mid = (L + R) // 2

            if nums[R] < nums[mid]:

                L = mid + 1
            
            else:

                R = mid
        
        partition_point = R

        left_partition = nums[:partition_point] 
        right_partition = nums[partition_point:]

        if binary_search(left_partition) != -1:
            return binary_search(left_partition)
        
        elif binary_search(right_partition) != -1:
            return len(left_partition) + binary_search(right_partition)
        
        else:
            return -1 


        
        
        

