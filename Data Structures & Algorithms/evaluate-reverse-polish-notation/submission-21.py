class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        """
        O(n)
        """
        stk = []
        operators = ("+", "-", "/", "*")
        for token in tokens:
            
            if token not in operators:
                stk.append(int(token))
            
            elif token == "+":
                a = stk.pop()
                b = stk.pop()
                stk.append(a+b)

            elif token == "*":
                a = stk.pop()
                b = stk.pop()
                stk.append(a*b)

            elif token == "-":
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            
            elif token == "/":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(b/a))

        
        return stk[-1]