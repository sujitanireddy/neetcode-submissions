"""
Dijstraks: finding min cost/weight

Kruskals:  MST

[[0,0],[2,2],[3,3],[2,4],[4,2]]

minHeap = [4,6,6,6] 
visit = len(points)

TC: O(n**2)
SC: O(n)
"""

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minHeap = [(0,0)] #cost, idx
        visit = set()
        mincost = 0

        while len(visit) < len(points):

            cost, idx = heapq.heappop(minHeap)

            x,y = points[idx]

            if (x,y) in visit:
                continue

            visit.add((x,y))
            mincost += cost
            
            for i in range(len(points)):
                dist = abs(points[i][0] - x) + abs(points[i][1] - y)
                heapq.heappush(minHeap, (dist, i))
        
        return mincost
        


