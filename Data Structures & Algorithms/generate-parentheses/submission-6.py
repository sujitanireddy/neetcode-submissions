"""
                            (((             )))


                                        (

                                ((                ()

                            (((     (()       ()(    X

                        X       [((()]      
                                        
Open : 1
Close : 1

Notes:
- Open para should alwasy come first. If no open, we cannot close
- Open | Close counts in my recursive arguments
- We can close only if open > close
- We can open upton n


                (
            
            ((
        
        (((

        ((()

        ((())

        ((()))




"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        sol = []

        def dfs(openn, close):

            #base case
            if len(sol) == n * 2:
                res.append("".join(sol))
                return
            
            if openn < n:
                sol.append("(")
                dfs(openn+1, close)
                sol.pop()
            
            if openn > close:
                sol.append(")")
                dfs(openn, close+1)
                sol.pop()

        dfs(0,0)
        return res
        