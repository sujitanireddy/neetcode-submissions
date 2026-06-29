class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        no_char_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        res, sol = [], []

        def backtrack(i):

            #basecase
            if len(digits) == len(sol):
                res.append(''.join(sol[:]))
                return
            
            for char in no_char_map[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()


        backtrack(0)

        return res

        
