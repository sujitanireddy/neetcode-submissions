class Solution:
    def isValid(self, s: str) -> bool:
        
        #key (close) : value (open)

        close_to_open ={")" : "(", 
                        "}" : "{",
                        "]" : "["}
        stk = []

        for p in s:
            if p not in close_to_open:
                stk.append(p)
            if p in close_to_open:
                if stk and stk[-1] == close_to_open[p]:
                    stk.pop()
                else:
                    return False


        if stk:
            return False
        else:
            return True


