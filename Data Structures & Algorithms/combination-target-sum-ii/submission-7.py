class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res, sol = [], []
        n = len(candidates)

        def backtrack(i, cur_sum):

            #basecase
            if cur_sum == target:
                res.append(sol[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            sol.append(candidates[i])
            backtrack(i+1, cur_sum + candidates[i])
            sol.pop()

            while i < (n - 1) and candidates[i] == candidates[i+1]:
                i+=1 
            backtrack(i+1, cur_sum)

        backtrack(0,0)

        return res