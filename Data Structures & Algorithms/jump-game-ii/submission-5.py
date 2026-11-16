class Solution:
    def jump(self, nums: List[int]) -> int:
        L = R = 0
        jumps = 0
        jump_range = 0

        while R < len(nums) - 1:
            for i in range(L, R+1):
                jump_range = max(jump_range, nums[i] + i)
            L += 1
            R = jump_range
            jumps += 1
        
        return jumps