class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        """
                                1 2 3

                                []                         [1]
                            []       [2]         [1].               [1,2]
                        []    [3] [2]  [2,3]  [1] [1,3]    [1,3]        [1,2,3]

        """

        sol = []
        res = []

        def backtrack(i):

            if i == len(nums):
                res.append(sol[:])
                return
            
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res