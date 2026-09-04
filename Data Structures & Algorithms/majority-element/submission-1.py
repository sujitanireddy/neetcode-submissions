"""
5

3.5 > 

[5,5,1,1,1,5,5]

 
{5,5,1,1,1,5,5}

2

{
  5 : 4
  1 : 3
}

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res, count = 0, 0

        for n in nums: 

            if count == 0:
                res = n
            
            count += (1 if res == n else -1)

        return res 

