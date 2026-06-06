class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        rathik = []

        for op in operations:

            if op == "+":
                a = rathik[-1]
                b = rathik[-2]
                rathik.append(a+b)
            
            elif op == "D":
                a = rathik[-1]
                rathik.append(2 * a)
            
            elif op == "C":
                rathik.pop()
            
            else:
                rathik.append(int(op))

        summ = 0
            
        for val in rathik:
            summ += val
        
        return summ

