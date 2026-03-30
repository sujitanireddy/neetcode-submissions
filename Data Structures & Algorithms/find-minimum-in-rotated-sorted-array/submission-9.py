class Solution:
    def findMin(self, nums: List[int]) -> int:

        L = 0
        R = len(nums) - 1

        while L < R:

            mid = (L+R) // 2

            if nums[mid] > nums[R]:

                L = mid + 1
            
            elif nums[mid] < nums[R]:

                R = mid
            
        return nums[L]

