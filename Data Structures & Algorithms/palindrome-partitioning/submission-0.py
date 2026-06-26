class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, sol = [], []
        length = len(s)

        def backtrack(i):

            if i == length:
                res.append(sol.copy())
                return

            for j in range(i, length):
                partition = s[i:j+1]
                print(partition)
                if partition == partition[::-1]:
                    sol.append(partition)
                    backtrack(j+1)
                    sol.pop()
            
        backtrack(0)
        return res