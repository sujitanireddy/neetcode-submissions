class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []

        for token in tokens:
            
            if token == "+":
                val1, val2 = stk.pop(), stk.pop()
                stk.append(int(val1) + int(val2))
            
            elif token == "*":
                val1, val2 = stk.pop(), stk.pop()
                stk.append(int(val1) * int(val2))
            
            elif token == "-":
                val2, val1 = stk.pop(), stk.pop()
                stk.append(int(val1) - int(val2))
            
            elif token == "/":
                val2, val1 = stk.pop(), stk.pop()
                stk.append(int(val1) / int(val2))
            
            else:
                stk.append(token)
        
        return int(stk[0])