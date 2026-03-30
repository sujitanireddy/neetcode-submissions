class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))

        best = 1
        streak = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                streak += 1
            else:
                best = max(best, streak)
                streak = 1

        best = max(best, streak)
        return best

    