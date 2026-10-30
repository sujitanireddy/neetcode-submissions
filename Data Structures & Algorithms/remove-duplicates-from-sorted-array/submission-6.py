"""
    
L
           R 
[1,2,3,4,1]
   
   L
     R
[1,1,2,3,4]

       L
         R
[2,10,10,30,30,30]

"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        L = R = 1

        while R < len(nums):

            if nums[R] == nums[R-1]:
                R += 1
            
            else:
                nums[L] = nums[R]
                L += 1
                R += 1
        
        return L

