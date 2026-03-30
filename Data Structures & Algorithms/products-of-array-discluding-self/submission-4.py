class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix_array = [0] * n
        postfix_array = [0] * n
        output = [0] * n

        prefix_array[0] = 1
        product_by_far = 1
        for i in range(1, n):
            product_by_far *= nums[i-1]
            prefix_array[i] = product_by_far
        
        postfix_array[-1] = 1
        product_by_far = 1
        for i in range(n-2, -1, -1):
            product_by_far *= nums[i+1]
            postfix_array[i] = product_by_far
        
        for i in range(n):
            output[i] = prefix_array[i] * postfix_array[i]
        
        return output


        