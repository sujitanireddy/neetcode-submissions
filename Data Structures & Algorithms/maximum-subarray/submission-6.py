"""
[2,-3,4,-2,2,1,-1,4]
O(n**2)

Kadanes algorithm
 
      i
[2,-3,4,-2,2,1,-1,4]

curr_sum = 0
max_sum  = 2

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = 0
        max_sum = float("-inf")

        for num in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        
        return max_sum