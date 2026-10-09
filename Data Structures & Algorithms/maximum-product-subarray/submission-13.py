"""

2,4,-3,5

Modified Kandes algo

2   4   -3      5
2   8   -3      -15 
        -27
        
Conditions for produt
= +ve * +ve = +ve
= -ve * -ve = +ve
= -ve * +ve = -ve


1   -3  2
1   1   2
1   -3  -6

Track for min and max whlie keep track of maximum
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        curr_max, curr_min = 1, 1

        for n in nums:
            temp = curr_max 
            curr_max = max(n, temp * n, curr_min * n)
            curr_min = min(n, temp * n, curr_min * n)
            res = max(res, curr_max)
        
        return res