"""
     i G
 0 1 2 3 4
[1,2,0,1,0]









"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):

            if nums[i] + i >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False