class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol = []
        res = []

        def backtrack(i, summ):

            if i == len(nums):
                return
            
            if summ == target:
                res.append(sol[:])
                return
            
            if summ > target:
                return
            
            sol.append(nums[i])
            backtrack(i, summ + nums[i])
            sol.pop()

            backtrack(i+1, summ)
        
        backtrack(0,0)
        
        return res