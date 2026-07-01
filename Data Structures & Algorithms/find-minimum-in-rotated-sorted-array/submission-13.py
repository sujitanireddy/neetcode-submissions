class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """      L
                 R 
        [3,4,5,6,1,2]

        if M > R:
            L = mid + 1

        elif : 
            M = R

        """

        L = 0 
        R = len(nums) - 1

        while L < R:

            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1 
            
            else:
                R = mid
        
        return nums[R]