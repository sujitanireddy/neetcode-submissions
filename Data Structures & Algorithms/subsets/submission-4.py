class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res, sol = [], []

        n = len(nums)

        def backtrack(i):

            if n == i: #went out of bounds
                res.append(sol.copy())
                return
            
            #if we choose nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #if we don't choose
            backtrack(i+1)

        backtrack(0)

        return res