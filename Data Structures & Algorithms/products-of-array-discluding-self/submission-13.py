"""

[1,2,4,6]

 1  1  2  8
 48 24 6  1 
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix_arr = [1] * n
        postfix_arr = [1] * n
        res = [1] * n

        #build prefix arr
        running_prod = 1
        for i in range(1,n):
            running_prod *= nums[i-1] 
            prefix_arr[i] = running_prod
        
        #build postfix arr
        running_prod = 1
        for i in range(n-2,-1,-1):
            running_prod *= nums[i+1] 
            postfix_arr[i] = running_prod

        for i in range(n):
            res[i] = prefix_arr[i] * postfix_arr[i]
        
        return res