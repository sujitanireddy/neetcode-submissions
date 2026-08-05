class Solution:
    def isValid(self, s: str) -> bool:
        
        """
        ([{     }])

        

        hashmap : close : open
        If we encounter a closed bracket, compare with top of the stk and check if they are the same, if not return False

        TC: O(n)
        SC: O(n)
        """
        closetoOpen = { '}' : '{', ']' : '[', ')' : '('}
        stk = []

        for p in s:

            if p in closetoOpen:

                if stk and stk[-1] == closetoOpen[p]:

                    stk.pop()
                
                else:
                    return False
            
            else:
                stk.append(p)

        return len(stk) == 0