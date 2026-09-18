"""
[2,4,-3,5]

1,2,3


-1,-2,-3 

6
-3
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = float("-inf")
        currMin = 1
        currMax = 1

        for num in nums:
            temp = currMin * num
            currMin = min(currMax * num, temp , num)
            currMax= max(currMax * num, temp, num)
            res = max(res, currMax)
        
        return res