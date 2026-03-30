class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        prefix_prods = [0] * n
        postfix_prods = [0] * n
        output = [0] * n

        prefix_prods[0] = 1
        running_prefix_prod = 1
        for i in range(1, n):
            running_prefix_prod *= nums[i-1]
            prefix_prods[i] = running_prefix_prod
        
        #print(prefix_prods)
        
        postfix_prods[-1] = 1
        running_postfix_prod = 1
        for i in range(n-2, -1, -1):
            running_postfix_prod *= nums[i+1]
            postfix_prods[i] = running_postfix_prod
        
        #print(postfix_prods)

        for i in range(n):
            output[i] = prefix_prods[i] * postfix_prods[i]
        
        return output


        