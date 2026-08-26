"""
1 1 3 3
      
         r2 r1 t
2  9  8  3  6

2 9  10  12 16


t = max(t + r2, r1)
r2 = r1
r1 = temp

f(i) = max(nums[i] + f(i+2), f(i+1))

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        r1, r2, i = 0, 0, 0

        while i < len(nums):

            temp = max(nums[i] + r2, r1)
            r2 = r1 
            r1 = temp
            i += 1
        
        return r1
        







