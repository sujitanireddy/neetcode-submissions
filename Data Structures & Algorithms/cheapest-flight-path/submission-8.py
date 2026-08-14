"""
prices = [from, to, price]

Observations:
- Directed Graph
- no duplicate flights and no flights to self (no self loops)

  200   100 
0 ->  1 -> 2 
  300 |    | 100
      3 <--

djistra's stops remaining (not very efficient TC for this use case)
Bellman Ford's algorithm

(k+1 iterations)

            0  1   2   3
prices =   [0,200,300,500]
temp   =   [0,200,300,500]  

if prices[s] == float("inf"): continue
if prices[s] + p < temp[d]: temp[d] = prices[s] + p

TC: O(n * m) * k  where n is the time to iterate over all the edges and m is to make a copy of the array.
SC: O(n)

"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            temp = prices[:]

            for s, d, p in flights:

                if prices[s] == float("inf"):
                    continue
                
                if prices[s] + p < temp[d]:
                    temp[d] = prices[s] + p
            
            prices = temp

        return -1 if prices[dst] == float("inf") else prices[dst]













