class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        prefix_arr = [1] * length
        
        running_prefix = 1
        for i in range(1, length):
            running_prefix *= nums[i-1]
            prefix_arr[i] = running_prefix
        
        running_postfix = 1
        for i in range(length - 2, -1, -1):
            running_postfix *= nums[i+1]
            prefix_arr[i] *= running_postfix
        
        return prefix_arr