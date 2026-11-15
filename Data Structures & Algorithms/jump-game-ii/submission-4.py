"""

L
R
0   1   2   3   4   5

2   4   1   1   1   1

                                                        0 (2)

                                
                                        1(4)                            2(1)

                            
                            2(1)    3(1)    4(1)    5(1)
                                
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        L = R = 0
        jump = 0
        max_jump = 0

        while R < len(nums) - 1:

            for i in range(L, R+1):

                max_jump = max(max_jump, nums[i] + i)
            
            L += 1
            R = max_jump
            jump += 1
        
        return jump