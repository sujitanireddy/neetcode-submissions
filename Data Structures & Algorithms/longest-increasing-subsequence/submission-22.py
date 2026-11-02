class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            
            lis = 0

            for j in range(i + 1, len(nums)):

                if nums[i] < nums[j]:
                    lis = max(lis, dp[j])
            
            dp[i] += lis
                    
        return max(dp)