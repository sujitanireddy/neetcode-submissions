class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        L = 0 
        R = len(nums) - 1

        while L < R:

            mid = (L + R) // 2

            if nums[mid] > nums[-1]:
                L = mid + 1
            
            else:
                R = mid
        
        return nums[L]
                