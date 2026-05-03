class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #prefix products
        # left_products = [1,1,2,8]
        # right_products= [48,24,6,1]
        # [48,24,12,8]

        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        output_products = [1] * n

        product_so_far = 1
        for i in range(1, n):
            product_so_far *= nums[i-1] 
            left_products[i] = product_so_far
        
        product_so_far = 1
        for i in range(n-2, -1, -1):
            product_so_far *= nums[i+1] 
            right_products[i] = product_so_far
        
        for i in range(n):
            output_products[i] = left_products[i] * right_products[i]

        return output_products