class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #algorithm
        #Compute prefix products and postfix products and multiply them

        n = len(nums)
        prefix_products = [0] * n
        postfix_products = [0] * n
        output = [0] * n

        prefix_products[0] = 1
        product_so_far = 1
        for i in range(1, n):
            product_so_far *= nums[i-1]
            prefix_products[i] = product_so_far
        
        postfix_products[-1] = 1
        product_so_far = 1
        for i in range(n-2, -1, -1):
            product_so_far *= nums[i+1]
            postfix_products[i] = product_so_far
        
        for i in range(n):
            output[i] = prefix_products[i] * postfix_products[i]
        
        return output
        