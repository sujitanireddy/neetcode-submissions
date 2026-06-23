class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol, res = [] , []

        length = len(nums)

        def backtrack(i, running_sum):
            
            #basecase
            if running_sum == target:
                res.append(sol.copy())
                return
            
            if running_sum > target:
                return
            
            for j in range(i, length):

                sol.append(nums[j])
                backtrack(j, running_sum + nums[j])
                sol.pop()

        backtrack(0, 0)

        return res