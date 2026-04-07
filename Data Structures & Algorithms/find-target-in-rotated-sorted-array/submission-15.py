class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        L = 0 
        R = n - 1 

        while L < R:

            mid = (L+R) // 2

            if nums[mid] > nums[R]:

                L = mid + 1
            
            else:

                R = mid
        
        partition_point = R

        if nums[0] <= nums[n-1]:
            L, R = 0, n - 1

        elif target >= nums[0] and target <= nums[partition_point - 1]:
            L, R = 0, partition_point - 1

        else:
            L, R = partition_point, n - 1

        while L <= R:

            mid = (L+R) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                R = mid - 1
            
            else:
                L = mid + 1
        
        return -1 
