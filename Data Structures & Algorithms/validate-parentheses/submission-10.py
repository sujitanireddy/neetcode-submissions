class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []
        close_to_open_mapping = { '}' : '{', ']' : '[', ')' : '('}

        for char in s:

            if char in close_to_open_mapping:

                if stk and close_to_open_mapping[char] == stk[-1]:
                    stk.pop()
                
                else:
                    return False

            else:
                
                stk.append(char)
        
        if stk:
            return False
        else:
            return True