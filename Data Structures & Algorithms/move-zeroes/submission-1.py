class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

             L
                   R    
        [1 2 5 0 0 0]
        """
        L = 0
        for R in range(len(nums)):
            if nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
        

        