class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        sol, res = [], []

        n = len(nums)

        def backtrack(i):

            if n == i:
                res.append(sol.copy())
                return
            
            #if we did choose
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            
            #if we did not choose nums[i]
            while i < (n - 1) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)

        backtrack(0)

        return res

            