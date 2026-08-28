"""
[0,0],[2,2],[3,3],[2,4],[4,2]
    
      [0,0] [2,2],[3,3],[2,4],[4,2]
0,0 =   0     4     6     6     6
2,2 =   4     0     2     6     6
3,3 =.  6     2     0     3     2


MST of the graph.
Prims and Kruskals. Prims

visit = {(0,0), (2,2), (3,3)}
minHeap = [  6     6     6     6     6, ]
minHeap = [cost(edges)]

while len(visit) < len(points):

TC: VlogE
SC: V + E
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        min_cost = 0
        visit = set()
        minHeap = [(0,points[0][0],points[0][1])] #cost, src node

        while len(visit) < len(points):

            cost, x, y = heapq.heappop(minHeap)

            if (x,y) in visit:
                continue

            visit.add((x,y))
            min_cost += cost

            for xi, yj in points:
                if (xi,yj) not in visit:
                    heapq.heappush(minHeap, (abs(x-xi) + abs(y-yj),xi,yj))

        return min_cost