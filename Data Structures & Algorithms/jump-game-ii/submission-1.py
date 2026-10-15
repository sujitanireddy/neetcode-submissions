"""
          G
0 1 2 3 4 5
2,4,1,1,1,1


0 0 3 2 1 0

res = float("inf")

i + nums[i] >= goal:
    dp[i] = dp[goal] + nums[i]
    res = min(dp[i],res)

"""
class Solution:
    def jump(self, nums: List[int]) -> int:

        res = 0
        L = R = 0
        farthest = 0

        while R < len(nums) - 1:

            for i in range(L, R+1):
                farthest = max(farthest, i + nums[i])

            L = R + 1
            R = farthest
            res += 1
        
        return res