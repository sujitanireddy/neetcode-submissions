"""
dijsktra's
Bellman Ford's algo

Kth iter
          0  1   2   3
prices = [0,inf,inf,inf]

temp   = [0,200,inf,inf]

K + 1 iter
prices = [0,200,inf,inf]

temp =   [0,200,300,500]

prices = [0,200,300,500]

                      s d  p    
[[0,1,200],[1,2,100],[1,3,300],[2,3,100]]
 

if prices[s] + p < temp[d]
    temp[d] = p + prices[s]

"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k+1):

            temp = prices.copy()

            for s, d, p in flights:

                if prices[s] + p < temp[d]:
                    temp[d] = p + prices[s]
                
            prices = temp
        
        return -1 if prices[dst] == float("inf") else prices[dst]