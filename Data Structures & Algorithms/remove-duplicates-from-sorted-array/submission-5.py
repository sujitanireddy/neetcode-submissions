"""
   
         R
[1,2,3,4,1]


       
[1,2,3,4,x]

          R
[2,10,30,10,30,30]

      
    L
      R    
1,2,1,2,2

"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        L = 1
        for R in range(1, len(nums)):

            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L += 1
        
        return L

                


