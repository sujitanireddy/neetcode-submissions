"""
 0 1 2 3 4
 G
[1,2,0,1,0]

i + nums[i] >= g:
    g = i

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0