class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Algorithm
        #Binary search for the min in rotated sorted array.
        #Slice the array into two sub arrays and binary search them.

        def binary_search(L, R):

            while L <= R:

                mid = (L + R) // 2

                if nums[mid] == target:
                    return mid

                elif nums[mid] > target:
                    R = mid - 1

                else:
                    L = mid + 1

            return -1 

        n = len(nums)
        L = 0
        R = n - 1

        while L < R:

            mid = (L + R) // 2

            if nums[R] < nums[mid]:

                L = mid + 1
            
            else:

                R = mid
        
        partition_point = R

        
        if partition_point == 0:
            return binary_search(L=0, R=n-1)
        
        elif target >= nums[0] and target <= nums[partition_point - 1]:
            return binary_search(L=0, R = partition_point - 1)
        
        else:
            return binary_search(L = partition_point, R = n - 1)

        
        
        

