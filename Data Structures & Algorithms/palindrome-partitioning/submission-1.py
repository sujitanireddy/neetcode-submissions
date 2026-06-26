class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, sol = [], []
        length = len(s)

        def ispali(partition):
            L = 0 
            R = len(partition) - 1

            while L < R:
                if partition[L] != partition[R]:
                    return False
                L+=1
                R-=1
            
            return True

        def backtrack(i):

            if i == length:
                res.append(sol.copy())
                return

            for j in range(i, length):
                partition = s[i:j+1]
                if ispali(partition):
                    sol.append(partition)
                    backtrack(j+1)
                    sol.pop()
            
        backtrack(0)
        return res



