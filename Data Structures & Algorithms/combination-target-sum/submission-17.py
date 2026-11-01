class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol = []
        res = []

        def backtrack(i):

            if sum(sol) > target:
                return

            if sum(sol) == target:
                res.append(sol[:])
                return

            if i >= len(nums):
                return

            #kepp choosing
            sol.append(nums[i])
            backtrack(i)
            sol.pop()

            #skip
            backtrack(i+1)
    
        backtrack(0)
        return res
