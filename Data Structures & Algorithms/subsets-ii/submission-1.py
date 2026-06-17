class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        sol, res = [], []
        n = len(nums)

        def backtracking(i):

            if i == n:
                res.append(sol.copy())
                return
            
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()

            while i < (n-1) and nums[i] == nums[i+1]:
                i += 1
            
            backtracking(i+1)
        
        backtracking(0)

        return res
