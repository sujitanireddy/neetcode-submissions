"""
TC: 2*n
                                                []
                                
                                          [1]          []

                               [1,2]             [1]         [2]     []
                        
                        [1,2,3]     [1,2]   [1,3]   [1] [2,3]   [2] [3] []





"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        res = []

        def backtrack(i):
            
            if i >= len(nums):
                res.append(sol.copy())
                return
            
            #choose
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            #skip
            backtrack(i+1)

        backtrack(0)
        return res