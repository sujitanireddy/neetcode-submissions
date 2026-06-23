class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol, res = [] , []

        length = len(nums)

        def backtrack(i):
            
            #basecase
            if sum(sol) == target:
                res.append(sol.copy())
                return
            
            if sum(sol) > target:
                return
            
            for j in range(i, length):
                sol.append(nums[j])
                backtrack(j)
                sol.pop()

        backtrack(0)

        return res