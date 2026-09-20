"""
[,2,1,2,2

[7,34,1,2,8

[(100,1),(80,1),



"""
class StockSpanner:

    def __init__(self):
        self.stk = [] 

    def next(self, price: int) -> int:

        span = 1

        while self.stk and price >= self.stk[-1][0]:

            stk_price, stk_span = self.stk.pop()
            span += stk_span

        self.stk.append((price, span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)