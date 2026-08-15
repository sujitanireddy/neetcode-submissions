"""
     
[2,1,1,2]

(0,2), (2,2), (2,3) (3,4)

temp = 2
rob_1 = 0
rob_2 = 0



f(i) = max(nums[i] + f(i+2), f(i+1))

"""

class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
            

        