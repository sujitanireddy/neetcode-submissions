class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol, res = [], []
        length = len(nums)
        summ = 0

        def backtrack(i, summ):

            if summ == target:
                res.append(sol.copy())
                return
            
            if summ > target:
                return
            
            for j in range(i, length):
                sol.append(nums[j])
                backtrack(j, summ + nums[j])
                sol.pop()
        
        backtrack(0, 0)

        return res