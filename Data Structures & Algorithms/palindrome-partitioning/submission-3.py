class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res, sol = [], []

        #def is_pali(string):
            #palindrom logic
        
        def backtrack(i):

            #basecases
            if i == len(s):
                res.append(sol[:])
                return
            
            for j in range(i, len(s)):
                string = s[i:j+1]
                if string == string[::-1]:
                    sol.append(string)
                    backtrack(j+1)
                    sol.pop()
        
        backtrack(0)
        return res