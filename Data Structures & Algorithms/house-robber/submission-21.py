"""
        
[1,1,3,3]

f(i) = max(nums[i] + f(i+2), f(i+1))


r2  r1  t
2   9   8   3   6


2   9   10  12  16


9   10

rob1, rob2, temp



"""
class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0

        for i in range(len(nums)):

            temp = max(nums[i] + rob2, rob1)
            rob2 = rob1
            rob1 = temp

        return rob1
        

            