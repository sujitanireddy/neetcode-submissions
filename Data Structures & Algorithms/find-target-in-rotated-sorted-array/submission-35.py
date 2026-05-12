class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #find min in rotated sorted array
        #find target in sub array using BS

        L = 0
        R = len(nums) - 1

        while L < R:

            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1 
            
            else:
                R = mid
        
        pivot = L
        
        if nums[0] <= nums[-1]:
            L = 0
            R = len(nums) - 1
        elif nums[0] <= target <= nums[pivot - 1]:
            L = 0
            R = pivot - 1
        else:
            L = pivot
            R = len(nums) - 1

        while L <= R:

            mid = (L+R) // 2

            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                L = mid + 1
            
            else:
                R = mid - 1
            
        return -1