class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #we need a open parantheses to close it.
        
        res, sol = [], []
        openn, close = 0, 0

        def backtrack(openn, close):

            if 2 * n == len(sol):
                res.append(''.join(sol))
                return
            
            if openn < n:
                sol.append('(')
                backtrack(openn + 1, close)
                sol.pop()
            
            if openn > close:
                sol.append(')')
                backtrack(openn, close + 1)
                sol.pop()
        
        backtrack(openn, close)
        return res