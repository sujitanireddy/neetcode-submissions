"""                                    s d. p
n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1

TC: O(k * n)
SC: O(n)

          0   1    2    3

prices = [0, inf, inf, inf]

temp =   [0, inf, inf, inf]

--------------------------------

prices = [0, 200, inf, inf]

temp =   [0, 200, inf, inf]



200 + 100 < inf
200 + 300 <

"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):

            temp = prices.copy()

            for s, d, p in flights:

                if prices[s] == float("inf"):
                    continue

                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            
            prices = temp

        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]

