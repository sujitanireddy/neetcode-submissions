class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        """
        ["1","2","+","3","*","4","-"]

        sub = b - a
        div = b - a

        """
        stk = []
        for token in tokens:
            if token == "+":
                a = stk.pop()
                b = stk.pop()
                stk.append(a+b)
            elif token == "*":
                a = stk.pop()
                b = stk.pop()
                stk.append(a*b)
            elif token == "/":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b/a))
            elif token == "-":
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            else:
                stk.append(int(token))

        return stk[0] 

