"""
       i
[5,5,1,1,1,5,5]

res = 1
freq = 1


7 // 2 = 3 

[2,2,2]

3/2 = 1

TC: O(nlogn)
SC: O(1)


"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        res = 0
        freq = 0
        
        for i in range(len(nums)):

            if freq == 0:
                res = nums[i]
            
            if nums[i] != res:
                freq -= 1
            else:
                freq += 1
        
        return res