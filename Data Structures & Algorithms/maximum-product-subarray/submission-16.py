"""
    2, 4,  -3, 5

min 2  8  -24  -120
max 2  8   8    8  

 -ve -ve = value decreses
 -ve +ve = value decreses

"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        currMin = 1
        currMax = 1
        res = float("-inf")

        for n in nums:

            temp = n * currMin
            currMin = min(n, temp , n * currMax)
            currMax = max(n, n * currMax, temp)
            res = max(res, currMax)
        
        return res