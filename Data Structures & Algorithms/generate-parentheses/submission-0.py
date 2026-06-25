class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        sol, res = [], []

        open_count, close_count = 0, 0 

        def backtrack(open_count, close_count):

            if len(sol) == n * 2:
                res.append(''.join(sol.copy()))
                return
            
            if open_count < n:
                sol.append('(')
                open_count += 1
                backtrack(open_count, close_count)
                open_count -= 1
                sol.pop()
            
            if open_count > close_count:
                sol.append(')')
                close_count += 1
                backtrack(open_count, close_count)
                close_count -= 1
                sol.pop()
        
        backtrack(0,0)
        return res
