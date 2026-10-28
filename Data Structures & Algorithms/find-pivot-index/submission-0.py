"""
 1 8 11 17 22 28
        17  11   6
[1,7,3, 6, 5, 6]



"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix_arr = []
        postfix_arr = [0] * len(nums)

        prefix = 0
        for n in nums:
            prefix += n
            prefix_arr.append(prefix)
        
        postfix = 0
        for i in range(len(nums) - 1, -1, -1):
            postfix += nums[i]
            postfix_arr[i] = postfix
        
        for i in range(len(postfix_arr)):
            if prefix_arr[i] == postfix_arr[i]:
                return i
        
        return -1