class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {'+', '-', '*', '/'}
        new_value = 0
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if stack:
                    if token == '+':
                        first_value = stack.pop()
                        second_value = stack.pop()
                        new_value = second_value + first_value
                        stack.append(new_value)
                    elif token == '*':
                        first_value = stack.pop()
                        second_value = stack.pop()
                        new_value = second_value * first_value
                        stack.append(new_value)
                    elif token == '-':
                        first_value = stack.pop()
                        second_value = stack.pop()
                        new_value = second_value - first_value
                        stack.append(new_value)
                    elif token == '/':
                        first_value = stack.pop()
                        second_value = stack.pop()
                        new_value = int(second_value / first_value)
                        stack.append(new_value)
                    
        return stack.pop()

            