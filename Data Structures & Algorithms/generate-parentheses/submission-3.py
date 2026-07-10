class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        """
                                          (
                                     ()       ((     
                                
                                ()(     X

                            ()()  ()((
        Observations
        - Need open bracket first to close
        - We can open uptill "n" brackets - Basecase for opening
        - open count > close count to close - Basecase for closing
        """

        res = []
        sol = []

        def backtrack(openn, close):

            if len(sol) == n * 2:
                res.append("".join(sol[:]))
                return
            
            if openn < n:
                sol.append("(")
                backtrack(openn + 1, close)
                sol.pop()
            
            if openn > close:
                sol.append(")")
                backtrack(openn, close + 1)
                sol.pop()
        
        backtrack(0,0)
        return res



            

