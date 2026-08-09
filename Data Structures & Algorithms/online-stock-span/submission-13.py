"""
7 2 1 2

today: 2

[100,80,60,70,60,75,85]

[(100,1),(80,1),(60,1),(70,2),(60,1),]

#val, span

stk[-1][0] <= price: 
"""

class StockSpanner:

    def __init__(self):
        self.stk = []
        
    def next(self, price: int) -> int:
        span = 1

        while self.stk and self.stk [-1][0] <= price:
            stk_price, stk_span = self.stk.pop()
            span += stk_span

        self.stk.append((price, span))

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)