"""
     i 
[2,2,2]
 

             n
[5,5,1,1,1,5,5]

freq = 1
res = 5

if the freq = 0: update the value

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = 0
        res = 0

        for num in nums:

            if freq == 0:
                res = num
            
            if res != num:
                freq -= 1
            
            else:
                freq += 1
            
        return res
        