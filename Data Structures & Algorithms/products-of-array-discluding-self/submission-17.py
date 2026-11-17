class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
            
        # 0 1 2 3
        #[1,1,2,8]
        curr_prefix = 1
        for i in range(1, len(nums)):
            curr_prefix = nums[i-1] * curr_prefix
            res[i] *= curr_prefix
        
        curr_postfix = 1
        for i in range(len(nums)-2, -1, -1):
            curr_postfix = nums[i+1] * curr_postfix
            res[i] *= curr_postfix
        
        return res

