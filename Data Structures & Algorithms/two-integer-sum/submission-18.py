class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        diff_map = defaultdict(int)

        for i in range(len(nums)):

            diff = target - nums[i]
            
            if diff in diff_map:

                return [diff_map[diff], i]
            else:
                diff_map[nums[i]] = i 
        