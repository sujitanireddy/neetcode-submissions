class MinStack:

    # [1 
    #
    #

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

        val = min(self.minstk[-1], val) if self.minstk else val

        self.minstk.append(val)

    def pop(self) -> None:
        del self.stk[-1]
        del self.minstk[-1]

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
