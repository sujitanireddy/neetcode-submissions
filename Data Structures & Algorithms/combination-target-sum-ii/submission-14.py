class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        res = []
        sol = []

        def backtrack(i, summ):

            if summ == target:
                res.append(sol[:])
                return

            if summ > target:
                return

            if i == len(candidates):
                return
            
            sol.append(candidates[i])
            backtrack(i+1, summ + candidates[i])
            sol.pop()

            while i < (len(candidates) - 1) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, summ)

        backtrack(0, 0)

        return res