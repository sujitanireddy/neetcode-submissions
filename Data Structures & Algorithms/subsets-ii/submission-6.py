class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
       """
       []        [1]
     []  [2]    [1] [1,2]
   [] [1]

        Sort nums
        Skip duplicates in decicion tree
       """

       nums.sort()
       res = []
       sol = []

       def backtrack(i):

            #base case
            if i == len(nums):
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            while i < (len(nums) - 1) and nums[i] == nums[i+1]:
                i += 1
            
            backtrack(i+1)

       backtrack(0)

       return res