""" 
       L
           R 
[1,2,2,4,1]

{
  1 : 2
  2 : 1
  3 : 1
  4 : 1
}
TC : O(n)
SC:  O(n)
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        L = 1
        for R in range(1, len(nums)):

            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L += 1
        
        return L