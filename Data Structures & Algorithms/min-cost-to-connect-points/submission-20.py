"""

         4             2            2           4
(0,0)----------(2,2)------(3,3)--------(2,4)--------(4,2)

MST: Prims

TC: O(V+E)
SC: O(v**2)


"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minHeap = [(0,points[0][0],points[0][1])] #cost,x,y
        visit = set()
        res = 0

        while len(visit) != len(points):

            cost, x, y = heapq.heappop(minHeap)

            if (x,y) in visit:
                continue
            
            visit.add((x,y))
            res += cost

            for x1, y1 in points:
                dist = abs(x1 - x) + abs(y1 - y)
                heapq.heappush(minHeap, (dist, x1, y1))
        
        return res