"""

 L
     R
[0,0,1,2,0,5]

     L     R
[1,2,5,0,0,0]





"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        L = 0 

        for R in range(len(nums)):

            if nums[R] != 0:
                nums[R], nums[L] = nums[L], nums[R]
                L += 1
