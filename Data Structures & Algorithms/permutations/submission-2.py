class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        """
        permutations = n!

                                        []

                            [1]        [2]          [3]

                       [1,2]  [1,3] [2,1] [2,3] [3,1] [3,2]
                    
                    [1,2,3]   [1,3,2]

        Basecase
        - If len(sol) == len(nums)
        TC: 2 ** n
        SC: 2 ** n
        """
        res = []
        sol = []

        def backtrack():
        
            if len(sol) == len(nums):
                res.append(sol[:])
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return res