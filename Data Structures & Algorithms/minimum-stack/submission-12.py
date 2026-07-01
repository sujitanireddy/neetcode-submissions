class MinStack:

    """
    stk = [1]
    min_stk = [1]

    """

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val: int) -> None:

        self.stk.append(val)

        if self.minstk:
            self.minstk.append(min(self.minstk[-1], val))
        else:
            self.minstk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
