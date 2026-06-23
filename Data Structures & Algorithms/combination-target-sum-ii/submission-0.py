class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        sol, res = [], []
        length = len(candidates)
        summ = 0

        def backtrack(i, summ):

            if summ == target:
                res.append(sol.copy())
                return
            
            if summ > target:
                return
            
            for j in range(i, length):

                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if summ + candidates[j] > target:
                    continue
                    
                sol.append(candidates[j])
                backtrack(j+1, summ + candidates[j])
                sol.pop()

        backtrack(0,0)
        return res