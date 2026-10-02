"""
Kande's Algo

cases
- pos * pos = pos
- neg * neg = pos
- neg * pos or pos * neg = neg
- 0 * neg or pos = 0

    
2,4,-3,5

-3  0   -2

curmin = 0
curmax = 0

-3  0
1   0

"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float("-inf")
        curMin = 1
        curMax = 1

        for num in nums:
            temp = curMin * num
            curMin = min(num, temp, curMax * num)
            curMax = max(num, temp, curMax * num)
            res = max(res, curMin, curMax)

        return res
