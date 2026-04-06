class MinStack:

    def __init__(self):
        self.stk = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        

    def pop(self) -> None:
        if self.stk:
            del self.stk[-1]

    def top(self) -> int:
        if self.stk:
            return self.stk[-1]

    def getMin(self) -> int:
        if self.stk:
            min_value = float("inf")
            for val in self.stk:
                min_value = min(min_value, val)
        return min_value
        
        
