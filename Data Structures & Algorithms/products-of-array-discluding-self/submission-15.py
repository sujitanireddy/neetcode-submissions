"""

[1,2,4,6]

 1  1  2  8
 48 24 6  1 
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        res = [1] * n

        #build prefix arr
        running_prod = 1
        for i in range(1,n):
            running_prod *= nums[i-1] 
            res[i] = running_prod
        
        #build postfix arr
        running_prod = 1
        for i in range(n-2,-1,-1):
            running_prod *= nums[i+1]
            res[i] *= running_prod

        return res