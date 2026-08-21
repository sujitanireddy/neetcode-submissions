"""
[0,0],[2,2],[3,3],[2,4],[4,2]

Minimum Spanning Tree = Prims

[(6,2),(6,3),(6,4)]

visit = (0,0)

0,0
4
TC: log n**2
SC: O(n)
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minHeap = [(0,0)] #cost, idx
        visit = set()
        mincost = 0

        while len(visit) < len(points):

            cost, idx = heapq.heappop(minHeap)

            x, y = points[idx]

            if (x,y) in visit:
                continue

            visit.add((x,y))
            mincost += cost

            for j in range(len(points)):
                dist = abs(points[j][0] - x) + abs(points[j][1] - y)
                heapq.heappush(minHeap, (dist,j))
            
        return mincost