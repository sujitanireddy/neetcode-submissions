class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        sol, res = [], []

        def backtrack(i):

            if len(sol) == k:
                res.append(sol.copy())
                return
            
            if i > n:
                return
            
            #choose nums[i]
            sol.append(i)
            backtrack(i+1)
            sol.pop()

            backtrack(i+1)

        backtrack(1)
        return res