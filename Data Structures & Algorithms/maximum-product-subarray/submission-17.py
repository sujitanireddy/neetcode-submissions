class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMin, curMax = 1, 1
        maximum_prod = float("-inf")

        for num in nums:
            temp = curMin * num
            curMin = min(num, temp, curMax * num)
            curMax = max(num, curMax * num, temp)
            maximum_prod = max(curMax, maximum_prod)
        
        return maximum_prod
