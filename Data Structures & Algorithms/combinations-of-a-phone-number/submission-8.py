class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        num_letter_map = {'2' : 'abc', '3' : 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        sol = []
        res = []
        
        def dfs(i):

            if len(digits) == len(sol):
                res.append("".join(sol))
                return

            for j in range(i, len(digits)):
                for char in num_letter_map[digits[j]]:
                    sol.append(char)
                    dfs(j+1)
                    sol.pop()

        dfs(0)
        return res