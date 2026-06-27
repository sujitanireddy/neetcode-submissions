class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []
        summ = 0

        def backtrack(i, summ):

            if summ == target:
                res.append(sol[:])
                return
            
            if summ > target:
                return
            
            for j in range(i, len(nums)):
                sol.append(nums[j])
                backtrack(j, summ + nums[j])
                sol.pop()
        
        backtrack(0, summ)

        return res