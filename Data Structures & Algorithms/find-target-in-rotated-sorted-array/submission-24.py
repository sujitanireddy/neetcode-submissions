class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        L = 0 
        R = len(nums) - 1 

        while L < R:

            mid = (L + R) // 2

            if nums[mid] > nums[R]:

                L = mid + 1 
            
            else:

                R = mid
        
        pivot = R 

        if nums[pivot] <= target <= nums[-1]:
            L = pivot
            R = len(nums) - 1
        
        else:
            L = 0
            R = pivot - 1
        
        while L <= R:

            mid = (L + R) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                R = mid - 1
            
            else:
                L = mid + 1
        
        return -1

