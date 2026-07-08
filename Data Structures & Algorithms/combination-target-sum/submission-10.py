class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        """
        2 5 6 9 | target = 9

                                []
                            
                            [2]     []
                        
                        [2,2] [2,5] [5] []

                    [2,2,2]

                [2,2,2,2]

            [2,2,2,2,2]


        Base Cases
        - If sum > target: return
        - If sum == target: save the copy and return

        """
        res = []
        sol = []

        def backtrack(i, summ):

            if len(nums) == i:
                return

            if summ == target:
                res.append(sol[:])
                return
            
            if summ > target:
                return

            sol.append(nums[i])
            backtrack(i, summ + nums[i])
            sol.pop()
            
            backtrack(i+1, summ)

        backtrack(0, 0)
        return res
        