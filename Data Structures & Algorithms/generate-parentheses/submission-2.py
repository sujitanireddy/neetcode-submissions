class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res, sol = [], []
        openn, close = 0, 0

        def backtrack(openn, close):

            #base case
            if len(sol) ==  2 * n:
                res.append(''.join(sol[:]))
                return
            
            if openn < n:
                sol.append("(")
                backtrack(openn + 1, close)
                sol.pop()
            
            if openn > close:
                sol.append(")")
                backtrack(openn, close + 1)
                sol.pop()
            
        backtrack(openn, close)

        return res