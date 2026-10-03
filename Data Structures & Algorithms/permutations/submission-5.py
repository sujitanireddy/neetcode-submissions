"""
                        [1,2,3]

            [1]                     [2]

        [1,2]   [1,3]

    [1,2,3]         [1,3,2]


TC: 2**n
SC: 2**n
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        res = []

        def backtrack():
            
            if len(nums) == len(sol):
                res.append(sol.copy())
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return res