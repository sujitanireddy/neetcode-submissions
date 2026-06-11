class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        L = 0
        R = len(nums) - 1

        index = 0

        while L < R:

            mid = (L + R) // 2

            if target > nums[mid]:

                L = mid + 1 

            elif target < nums[mid]:

                index = mid

                R = mid

            else:
                return mid 
        
        if target > nums[-1]:
            return L + 1
        
        else:
            
            return L 