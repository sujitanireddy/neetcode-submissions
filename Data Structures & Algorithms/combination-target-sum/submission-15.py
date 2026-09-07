"""
                            [3,4,5]

                        [3]         []

                 [3,4]      [3]     [4]     []

                





"""


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        res = []
        sol = []
        
        def backtrack(i, summ):
        
            if summ > target:
                return 

            if summ == target:
                res.append(sol.copy())
                return

            if i >= len(nums):
                return

            sol.append(nums[i])
            backtrack(i, summ + nums[i])
            sol.pop()

            backtrack(i+1, summ)

        backtrack(0, 0)
        
        return res
