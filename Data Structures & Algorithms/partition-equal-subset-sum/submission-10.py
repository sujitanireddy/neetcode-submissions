"""
edge case: if sum(nums) % 2 != 0: return False

base cases: 
- if i == len(nums): return False
- if sum(nums) // 2 == summ: return Truen
- if sum(nums) // 2 < summ: return False

Memoization: o(n*target) and O(n*target)
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0: return False
        
        target = sum(nums) // 2

        cache = {}

        def dfs(i, summ):
            
            if (i,summ) in cache: 
                return cache[(i,summ)]
            
            if target == summ: 
                return True
            
            if summ > target: 
                return False

            if i == len(nums): 
                return False

            cache[(i,summ)] = dfs(i+1, summ + nums[i]) or dfs(i+1, summ)

            return cache[(i,summ)]

        return dfs(0,0)