class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        sol, res = [], []

        def backtrack(i):
            
            if n == i:
                res.append(sol.copy())
                return

            #include
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #don't include
            while i < (n - 1) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1)

        
        backtrack(0)
        return res