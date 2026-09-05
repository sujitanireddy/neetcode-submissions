class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        R = 0
        count = 0
        res = 0

        for R in range(len(nums)):
        
            if  count == 0:
                res = nums[R]	

            count += 1 if res == nums[R] else -1 
        
        return res
