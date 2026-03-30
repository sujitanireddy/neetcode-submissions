class Solution:
    def findMin(self, nums: List[int]) -> int:
        
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
        
        return min_so_far
