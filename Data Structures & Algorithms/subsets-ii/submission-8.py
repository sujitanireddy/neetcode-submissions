"""

                    [1, 2, 1]

                    [1]
                
            [1,2]        [1]

    [1,2,1]  [1,2]      [1,2]          [1]



"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        sol = []
        res = []

        def backtrack(i):

            if i >= len(nums):
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            while i <= len(nums) - 2 and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)

        

        backtrack(0)
        
        return res