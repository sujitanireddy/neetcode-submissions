"""
                [2,-3,4,-2,2,1,-1,4]

                        2           0
                    
                   -1       2     -3        0

TC: O(n)
SC: O(n)

 2 -1 4  2 4 5  4 8  
[2,-3,4,-2,2,1,-1,4]


- When we encounter a -ve number, make the running_max to 0
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float("-inf")
        curr_sum = 0

        for num in nums:

            curr_sum += num
            res = max(res, curr_sum)
            
            if curr_sum < 0:
                curr_sum = 0


        return res