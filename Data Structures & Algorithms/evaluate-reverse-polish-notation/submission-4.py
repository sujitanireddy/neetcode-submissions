class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {'+', '-', '*', '/'}

        stk = []

        for token in tokens:
            if token not in operators:
                stk.append(token)
            else:
                second_elemet = int(stk.pop())
                first_element = int(stk.pop())


                if token == '+':
                    element = first_element + second_elemet

                if token == '-':
                    element = first_element - second_elemet

                if token == '*':
                    element = first_element * second_elemet

                if token == '/':
                    element = first_element / second_elemet
                
                stk.append(element)
        
        return int(stk[-1])


