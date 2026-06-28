class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, sol = [], []
        n = len(s)

        def backtrack(i):

            #basecase
            if n == i:
                res.append(sol[:])
                return
            
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()
        
        backtrack(0)

        return res
