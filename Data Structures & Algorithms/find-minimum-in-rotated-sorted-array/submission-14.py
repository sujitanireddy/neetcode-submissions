class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """
        For binary search to work
            - sorted array
                R
                L 
        0 1 2 3 4 5
        3 4 5 6 1 2

        if R < mid: L = mid + 1

        """

        L = 0 
        R = len(nums) - 1

        while L < R:

            mid = (L+R) // 2

            if nums[R] < nums[mid]:
                L = mid + 1
            
            else:
                R = mid

        return nums[L]
