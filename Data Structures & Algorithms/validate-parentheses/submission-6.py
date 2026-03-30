class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closetoopen = {'}' : '{', ']' : '[', ')': '('}

        for parantheses in s:
            if parantheses in closetoopen:
                if stack and stack[-1] == closetoopen[parantheses]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(parantheses)
        
        if stack:
            return False
        else:
            return True


        