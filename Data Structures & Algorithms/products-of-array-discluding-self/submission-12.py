class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1 2 4 6
        48, 24
        O(n ** 2)

        TC: O(n)
        SC: O(n)

        prefix = [1,1,2,8]

        1 2 4 6

        1 


        postfix= [48,24,6,1]
        """

        n = len(nums)
        prefix_arr = [1] * n
        postfix_arr = [1] * n
        output_arr = [1] * n

        prefix_running_prod = 1
        for i in range(1, n):
            prefix_running_prod *= nums[i-1]
            prefix_arr[i] = prefix_running_prod

        running_prod = 1
        for i in range(n-2, -1, -1):
            running_prod *= nums[i+1]
            postfix_arr[i] = running_prod
        
        for i in range(n):
            output_arr[i] = prefix_arr[i] * postfix_arr[i]
        
        return output_arr