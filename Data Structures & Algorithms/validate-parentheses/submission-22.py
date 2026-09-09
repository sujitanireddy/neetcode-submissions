"""
( [ { } ] )

[([{]


{    {}
  

"""
class Solution:
    def isValid(self, s: str) -> bool:

        close_open_map = {')':'(', '}':'{', ']':'['}

        stk = []


        for p in s:

            if stk and p in close_open_map and close_open_map[p] == stk[-1]:
                stk.pop()

            else:
                stk.append(p)
        
        return len(stk) == 0
