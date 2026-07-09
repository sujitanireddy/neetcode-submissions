class StockSpanner:

    def __init__(self):
        
        self.stk = []

    def next(self, price: int) -> int:

        span = 1

        while self.stk and self.stk[-1][0] <= price:

            stk_price, stk_span = self.stk.pop()

            span += stk_span

        self.stk.append((price, span))

        return span        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


"""

[7,2,1,2  2

[7,34,1,2 8


O(n)

[ (100,1), (80, 1) (75,4)        ]


span = 1

while stk and stk[-1][1] <= price:
    stk_price, stk_span = stk.pop()
    span += stk_span

stk.append((prices, span))

TC: O(1)
SC: O(n)

"""