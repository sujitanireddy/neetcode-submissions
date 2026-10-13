class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashset = defaultdict(int)

        for i, num in enumerate(nums):
            if target - num in hashset:
                return [hashset[target - num], i]
            hashset[num] = i
