class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sol = []

        def backtrack(i):

            #basecase
            if len(nums) == i:
                res.append(sol[:])
                return
            
            #choose nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #don't choose nums[i]
            backtrack(i+1)
        
        backtrack(0)

        return res