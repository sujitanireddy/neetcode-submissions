class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

        if self.min_stk:
            val = min(self.min_stk[-1], val)

        self.min_stk.append(val)
    
    def pop(self) -> None:
        del self.stk[-1]
        del self.min_stk[-1]

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]
