"""                         i
                                    j       
                            a   a   b

                            [a]     [aa]        [aab]X
                        
                        [a,a]       [aa, b]
                    
                    [a,a,b]

- out of bound, add array the res

TC: O(n**3)
SC: O(n**2)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        sol = []
        res = []

        def backtrack(i):
            
            if i >= len(s):
                res.append(sol.copy())
                return
            
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()

        backtrack(0)
        return res