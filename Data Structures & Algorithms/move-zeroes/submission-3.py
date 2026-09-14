"""
       L
           R 
[1,2,5,0,0,0,]

   L   R
[1,0,0,2,0,5]

L
  R
1,2,3,4,5

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        for R in range(len(nums)):
            if nums[R] != 0:
                nums[L],nums[R] = nums[R],nums[L]
                L += 1
         