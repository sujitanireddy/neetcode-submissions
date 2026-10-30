class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_idx_map = defaultdict(int) #diff : i
    
        for i, n in enumerate(nums):
            if target - n in diff_idx_map:
                return [diff_idx_map[target - n],i]
            else:
                diff_idx_map[n] = i