class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        no_letter_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        sol, res = [], []

        k = len(digits)

        def backtrack(i):

            if len(sol) == k:
                res.append(''.join(sol.copy()))
                return
            
            for letter in no_letter_map[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)

        return res