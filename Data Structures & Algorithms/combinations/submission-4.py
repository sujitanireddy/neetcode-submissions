class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        sol, res = [], []

        def backtrack(i):

            for j in range(i, n+1):
                sol.append(j)
                if len(sol) == k:
                    res.append(sol.copy())
                else:
                    backtrack(j+1)
                sol.pop()
        
        backtrack(1)
        return res
