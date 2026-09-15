class Solution:
    def canJump(self, nums: List[int]) -> bool:

        cache = {}

        target = len(nums) - 1
        
        def dfs(i):

            if i in cache:
                return cache[i]
            
            if i == target:
                return True
            
            if i > target:
                return False
            
            for j in range(1, (nums[i] + 1)):
                cache[i] = dfs(i+j)
                if cache[i] == True:
                    return True
            
            return False

        return dfs(0)

