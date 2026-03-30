class Solution:
    def isValid(self, s: str) -> bool:

        stk = []
        opentoclose = {")": "(", ']': '[', '}': '{'} #keys ), }, ]

        for paranthese in s:

            #if paranthese is open
            if paranthese not in opentoclose:
                stk.append(paranthese)

            else:
                if stk and stk[-1] == opentoclose[paranthese]:
                    stk.pop()
                else:
                    return False
                
        if stk:
            return False
        
        else:
            return True

        




        
        


            
            











        