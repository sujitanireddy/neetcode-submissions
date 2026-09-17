"""
      2, 4,  -3,  5 
min   2  4.  
max   2. 8

2,8,-24,-120

[-3,0,-2]
-3,0,0

[-10,1,-10,10]
 currmin = -10 
 currmax =  1
 

  max = 10
  min = 2

if we see a -ve value, it makes sense to multiply min val



 -10 -10, 10, 10

3 conditions:
-ve * -ve = +ve value = we need this
-ve * +ve = -ve value = we dont need this
+ve * +ve = we need

"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = float("-inf")
        curMax, curMin = 1, 1

        for num in nums:

          temp = num * curMax
          curMax = max(temp, num * curMin, num)
          curMin = min(temp, num * curMin, num)
          res = max(res, curMax)
        
        return res





















        
        


