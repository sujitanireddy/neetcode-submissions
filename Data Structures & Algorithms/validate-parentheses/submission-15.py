class Solution:
    def isValid(self, s: str) -> bool:
        
        """
        hashmap : {close:open}
        
        ( [ { } ] )

        [ == ]         ]

        if closing bracket and top of the stk == open bracket of the same type
            pop
        

        """

        open_to_close = {')':'(', '}':'{', ']':'['}

        stk = []

        for p in s:

            if stk and p in open_to_close and stk[-1] == open_to_close[p]:
                stk.pop()
            
            else:
                stk.append(p)

        return len(stk) == 0 


