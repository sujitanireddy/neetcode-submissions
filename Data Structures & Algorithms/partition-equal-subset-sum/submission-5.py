class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)
        half_sum = total_sum / 2

        if total_sum % 2 != 0:
            return False

        cache = {}

        def dfs(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]
            
            if summ > half_sum:
                return False

            if summ == half_sum:
                return True

            if i == len(nums):
                return False

            cache[(i,summ)] = dfs(i+1, summ + nums[i]) or dfs(i+1, summ)

            return cache[(i,summ)]
        
        return dfs(0,0)

