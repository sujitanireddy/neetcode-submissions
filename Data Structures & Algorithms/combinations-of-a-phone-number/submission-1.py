class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res, sol = [], []
        length = len(digits)

        def backtrack(i):

            if length == len(sol):
                res.append(''.join(sol.copy()))
                return
            
            for char in phone_map[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)

        return res