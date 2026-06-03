class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #[1,2,4,6]
        #[1,1,2,8] #leftprefix
        #[48,24,6,1] #rightprefix

        length = len(nums)
        left_prefix = [1] * length
        right_prefix = [1] * length
        output = [1] * length

        max_left = 1
        for i in range(1, length):
            max_left *= nums[i-1]
            left_prefix[i] = max_left

        max_right = 1
        for i in range((length - 2), -1, -1):
            max_right *= nums[i+1]
            right_prefix[i] = max_right
        
        for i in range(length):
            output[i] = left_prefix[i] * right_prefix[i]
        
        return output
        
       