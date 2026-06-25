class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res, sol = [], []
        length = len(nums)

        def backtrack(i):

            if i == length:
                res.append(sol.copy())
                return
            
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            while i < (length - 1) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1)

        backtrack(0)
        return res