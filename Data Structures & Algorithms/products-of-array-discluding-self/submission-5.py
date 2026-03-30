class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [0] * n
        prefix_products = [0] * n
        postfix_products = [0] * n

        prefix_products[0] = 1
        prefix_product_by_far = 1
        for i in range(1, n):
            prefix_product_by_far *= nums[i - 1]
            prefix_products[i] = prefix_product_by_far
        print(prefix_products)
        
        postfix_products[-1] = 1
        postfix_product_by_far = 1
        for i in range(n-2, -1, -1):
            postfix_product_by_far *= nums[i+1]
            postfix_products[i] = postfix_product_by_far

        for i in range(n):
            output[i] = prefix_products[i] * postfix_products[i]
        
        return output
            
        