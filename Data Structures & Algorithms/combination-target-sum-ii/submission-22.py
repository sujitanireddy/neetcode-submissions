"""
     i
[9,2,2,4,6,1,5], target = 8

     i
 0 1 2
[1,2,2]


                                            [1]         []
                                        
                                    
                                    [1,2]       [1]     [2]     []

                    [1,2,2]     [1,2]       [1,2]. [1]. [2,2]   [2]     [2]     []


Algorithm:
- Sort Candidates
- Recursivly do backtracking funciton 
- return res
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        
        res = []
        sol = []

        def backtrack(i, summ):
            
            #base cases
            if summ == target:
                res.append(sol.copy())
                return

            if i >= len(candidates):
                return
            
            if summ > target:
                return

            #choose the number
            sol.append(candidates[i])
            backtrack(i+1, summ + candidates[i])
            sol.pop()

            #don't choose
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1

            backtrack(i+1, summ)

        backtrack(0,0)

        return res





