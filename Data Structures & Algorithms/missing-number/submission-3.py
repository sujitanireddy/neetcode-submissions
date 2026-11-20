class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = 0
        for i in range(len(nums) + 1):
            x = x ^ i
        
        y = 0
        for n in nums:
            y = y ^ n
        
        return x ^ y

