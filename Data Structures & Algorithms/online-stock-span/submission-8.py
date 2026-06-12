class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:

        span = 1

        while self.stk and price >= self.stk[-1][0]:
            stk_p, stk_span = self.stk.pop()
            span += stk_span

        self.stk.append((price, span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

#[(100,1), (80,1), ]       (60,1)


# while stk and price >= stk[-1][0]:
#monotonically decreasing stack