class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diffrences_index = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diffrences_index:
                return [diffrences_index[diff], i]
            
            diffrences_index[n] = i