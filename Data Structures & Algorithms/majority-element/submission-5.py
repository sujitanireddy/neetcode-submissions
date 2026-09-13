"""
5,5,1,1,1,5,5
 
1 1 1 5 5 5 5 TC: O(nlogn) SC:O(1)

            i
5,5,1,1,1,5,5 

1 2 1 0 1 0 1 

res = 5
freq = 1

if  freq == 0:
    res = nums[i]
    freq += 1

elif nums[i] == res:
    freq += 1

else:
    freq -= 1

"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = 0
        freq = 0

        for num in nums:

            if num == res:
                freq += 1
            
            elif freq == 0:
                res = num
                freq += 1
            
            else:
                freq -= 1
        
        return res





























