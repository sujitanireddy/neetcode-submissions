"""
 0 1 2 3 4 5
[2,4,1,1,1,1] 
     L
            R



"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_range = 0
        L = R = 0
        res = 0

        while R < len(nums) - 1:
            for i in range(L, R+1):
                max_range = max(max_range, nums[i] + i)
            R = max_range
            L += 1
            res += 1
        
        return res