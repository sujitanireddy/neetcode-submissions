class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        sol = []

        def backtrack(i):

            if i == len(s):
                res.append(sol[:])
                return
            
            for j in range(i, len(s)):

                partition = s[i:j+1]

                if partition == partition[::-1]:

                    sol.append(partition)
                    backtrack(j+1)
                    sol.pop()
        

        backtrack(0)

        return res
