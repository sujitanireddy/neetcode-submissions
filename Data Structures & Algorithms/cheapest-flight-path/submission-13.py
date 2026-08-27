"""
[[0,1,200],[1,2,100],[1,3,300],[2,3,100]]

Bellman Ford

iterate k+1

Iteration 1
           0   1   2   3
prices = [ 0, inf,inf,inf]
temp =   [ 0, 200,inf,inf]

Iteration 2
             0.  1.  2. 3
prices =   [ 0, 200,inf,inf]
temp =     [ 0, 200,300,500]

             0  1    2.   3
temp =     [ 0, 200,300,500]

[s,d,p]

iterating over the flights

0 -> 1 : 200
1 -> 2 : 100

p + prices[s] < temp[d]:
temp[d] = p + prices[s]

300 + 200 < inf
1 3 300

[2,3,100]

100 + inf < 500

TC: O(N * k)
SC: O(n)
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k+1):
            temp = prices[:]

            for s,d,p in flights:
                if p + prices[s] < temp[d]:
                    temp[d] = p + prices[s]

            prices = temp
        
        return -1 if prices[dst] == float("inf") else prices[dst]

                




























