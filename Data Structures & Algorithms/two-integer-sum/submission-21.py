class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictt = {}

        for i in range(len(nums)):

            if (target - nums[i]) in dictt:

                return [dictt[target - nums[i]], i] 

            dictt[nums[i]] = i

            
