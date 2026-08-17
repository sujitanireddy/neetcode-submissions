"""
Notes:
- [from, to, price]

adjList: graph representation

dijkstra's

bellmen ford 

2 iter: (K+1)

1st iter: 
         0  1.  2   3
prices: [0,inf,inf,inf]
temp:   [0,200,inf,inf]

2nd iter:
         0  1.  2   3
prices: [0,200,inf,inf] -> [0,200,300,500]
temp:   [0,200,300,500]

Building the adjList: O(n + k)
SC: O(n)

from_i = 1
to_i = 2
p = 100




"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        #print(prices)
        for i in range(k+1):

            temp = prices[:]

            for s, d, p in flights:

                #if prices[s] == float("inf"):
                    #continue

                if p + prices[s] < temp[d]:
                    temp[d] = p + prices[s]
                    print(temp)
            
            print("first done")
            prices = temp
            
            
            
            #print(prices)
        
        return -1 if prices[dst] == float("inf") else prices[dst]

       