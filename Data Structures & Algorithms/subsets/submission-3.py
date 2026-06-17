class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sol, res = [], []
        n = len(nums)

        def backtrack(i):

            if n == i:
                res.append(sol.copy())
                return
            
            #select
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #don't select
            backtrack(i+1)

        backtrack(0)
        return res