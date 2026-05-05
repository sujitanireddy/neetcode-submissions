class Solution:
    def isValid(self, s: str) -> bool:
        
        #       ([{}])  []
        # hashmap: {closing:opening}

        closetoopen = {'}':'{', ')':'(', ']':'['}

        stk = []

        for p in s:

            if stk and p in closetoopen and closetoopen[p] == stk[-1]:
                stk.pop()

            else:
                stk.append(p)

        return len(stk) == 0