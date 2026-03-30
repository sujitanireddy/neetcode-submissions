class Solution:
    def isValid(self, s: str) -> bool:

        closetoopen = { '}' : '{', 
                        ')' : '(',
                        ']' : '[' } 
        
        stack = []

        for para in s:
            if para not in closetoopen:
                stack.append(para)
            else:
                if stack and stack[-1] == closetoopen[para]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        else:
            return True



        
        