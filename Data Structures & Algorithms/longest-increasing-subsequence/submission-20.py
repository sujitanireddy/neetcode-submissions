"""
      i
0 1 2 3 4 5 6
9,1,4,2,3,3,7


i=0                    1                                    0     

i=1               X       1(9)                   1(1)                0

i=2                      X      1(9)           X    1(1)    1(4)            0

i=3                             

2*n

O(n)
O(n)

O(n)
O(n)

0 1 2 3 4 5 6
9,1,4,2,3,3,7

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LIS = 0
        dp = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):

            LIS = 0

            for j in range(i+1, len(nums)):

                if nums[i] < nums[j]:
                    LIS = max(dp[j], LIS)
            
            dp[i] += LIS
        
        return max(dp)
        
