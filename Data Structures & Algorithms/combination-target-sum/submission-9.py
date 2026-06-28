class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []
        n = len(nums)

        def backtrack(i, cur_sum):

            #base cases 
            if cur_sum == target:
                res.append(sol[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            sol.append(nums[i])
            backtrack(i, cur_sum + nums[i])
            sol.pop()

            backtrack(i+1, cur_sum)

        backtrack(0, 0)

        return res