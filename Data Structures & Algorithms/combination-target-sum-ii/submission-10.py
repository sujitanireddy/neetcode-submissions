class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        """
                                    []
                                 [9]   []
                            X[9,2] [9] [2] []
                                 X[9,4] [9]  
    
        Basecases
        - If summ > target: return
        - if idx goes out of bounds: return
        - if summ == target: save the output and return

        Conditionals
        - Sort the input array to skip duplicates
        - We should not take the same decision again. That will lead to duplicate subsets
        """
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

            #choose decision path
            sol.append(candidates[i])
            backtrack(i+1, summ + candidates[i])
            sol.pop()

            #don't choose path
            while i < (len(candidates) - 1) and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, summ)

        
        backtrack(0, 0)
        return res