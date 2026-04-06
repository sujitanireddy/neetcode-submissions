class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        #algorithm
        #Use a stk and pop the last two elements and use the operator to compute and push back 
        #the resultant into stk and keep doing that until you traverse through the entire tokens


        stk = []

        for token in tokens:

            if token == "+":
                second_operand = int(stk.pop())
                first_operand = int(stk.pop())
                stk.append(first_operand + second_operand)
            
            elif token == "*":
                second_operand = int(stk.pop())
                first_operand = int(stk.pop())
                stk.append(first_operand * second_operand)
            
            elif token == "/":
                second_operand = int(stk.pop())
                first_operand = int(stk.pop())
                stk.append(first_operand / second_operand)
            
            elif token == "-":
                second_operand = int(stk.pop())
                first_operand = int(stk.pop())
                stk.append(first_operand - second_operand)
            
            else:
                stk.append(token)
        
        return int(stk.pop())