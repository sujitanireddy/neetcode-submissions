class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []

        for token in tokens:

            if token == "+":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(a)+int(b))
            
            elif token == "-":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b)-int(a))

            elif token == "*":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(a)*int(b))
            
            elif token == "/":
                a = stk.pop()
                b = stk.pop()
                stk.append(float(b)/float(a))

            else:
                stk.append(token)
        
        return int(stk[-1])

