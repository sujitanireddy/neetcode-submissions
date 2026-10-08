"""

2   2
1   1







"""


class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        
        if self.minstk:
            if val > self.minstk[-1]:
                min_val = self.minstk[-1]
                self.minstk.append(min_val)
            else:
                self.minstk.append(val)
        else:
            self.minstk.append(val)
        
    def pop(self) -> None:
        del self.stk[-1]
        del self.minstk[-1]

    def top(self) -> int:
        
        return self.stk[-1]
        

    def getMin(self) -> int:
        
        return self.minstk[-1]
