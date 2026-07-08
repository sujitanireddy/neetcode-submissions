class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        1,2,4,6
        Prefix algorithm? 
        prefix_prod = 1,1,2,8 O(n)
        postfix_prd = 48,24,6,1 O(n)
        """

        #TC: O(n)
        #SC: O(n)

        n = len(nums)
        prefix_prod = [1] * n
        postfix_prod = [1] * n
        output = [1] * n

        running_prod = 1
        for i in range(1, n):
            running_prod *= nums[i-1]
            prefix_prod[i] = running_prod

        postfix_running_prod = 1
        for i in range(n - 2, -1, -1):
            postfix_running_prod *= nums[i+1]
            postfix_prod[i] = postfix_running_prod
        
        for i in range(n):
            output[i] = prefix_prod[i] * postfix_prod[i]

        return output

