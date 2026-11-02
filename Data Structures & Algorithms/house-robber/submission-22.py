"""
 r2 r1 i 
[2, 9, 8 ,3,6]

 2  9  10   12  16



"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1 = rob2 = 0

        for i in range(len(nums)):
            temp = max(rob2 + nums[i], rob1)
            rob2 = rob1
            rob1 = temp
        
        return rob1
        

