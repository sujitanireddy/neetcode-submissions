class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #{value : idx}
        seen = defaultdict(int)

        for i, a in enumerate(nums):

            if target - a in seen:

                return [seen[target - a], i] 

            seen[a] = i
