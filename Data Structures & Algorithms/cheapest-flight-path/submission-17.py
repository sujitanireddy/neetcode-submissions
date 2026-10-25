"""

n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1

Notes:
- Bellman Ford
- O(V+E)
- O(V+E)
          0    1    2   3
prices = [0, inf, inf, inf] 
temp =   [0, inf, inf, inf]

          0    1    2   3
prices = [0, 200, 300, 500] 
temp =   [0, 200, inf, inf]

prices = [0, 200, 300, 500] 
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):

            temp = prices.copy()

            for s, d, p in flights:

                if prices[s] + p < temp[d]:

                    temp[d] = p + prices[s]
            
            prices = temp
        
        if temp[dst] == float("inf"):
            return -1
        
        else:
            return temp[dst]

