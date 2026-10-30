class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = R = 0

        while R < len(nums):

            if nums[R] != 0:
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
            
            R += 1