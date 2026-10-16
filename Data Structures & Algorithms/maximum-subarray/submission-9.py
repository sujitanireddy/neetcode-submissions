"""

     
2,-3,4,-2,2,1,-1,4

running_sum = 0
max_sum = 4
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        running_sum = 0
        max_sum = float("-inf")

        for i in range(len(nums)):
            running_sum += nums[i]
            max_sum = max(max_sum, running_sum)
            if running_sum < 0:
                running_sum = 0
        
        return max_sum
