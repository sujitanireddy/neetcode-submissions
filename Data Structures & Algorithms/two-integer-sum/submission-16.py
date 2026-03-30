class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff_hashamp = collections.defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in diff_hashamp:
                return [diff_hashamp[diff], i]
            
            diff_hashamp[nums[i]] = i