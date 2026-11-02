class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2

        cache = {}

        def dfs(i, summ):

            if (i,summ) in cache:
                return cache[(i,summ)]

            if summ == target:
                return True

            if summ > target:
                return False

            if i >= len(nums):
                return False
            
            skip, choose = False, False

            skip = dfs(i+1, summ)

            choose = dfs(i+1, summ + nums[i])

            cache[(i,summ)] =  skip or choose

            return cache[(i,summ)]
        
        return dfs(0,0)
