class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = candidates
        nums.sort()
        res, sol = [], []
        n = len(nums)

        def backtrack(i, cur_sum):

            #base case
            if cur_sum == target:
                res.append(sol[:])
                return
            
            #base case 2
            if cur_sum > target or n == i:
                return
            
            sol.append(nums[i])
            backtrack(i+1, cur_sum + nums[i])
            sol.pop()

            while i < n-1 and nums[i] == nums[i+1]:
                i+=1 
            backtrack(i+1, cur_sum)
        
        backtrack(0,0)

        return res