"""
MST = Prims

[[0,0][2,2],[3,3],[2,4],[4,2]]

0,0 -> 2,2 : 4
0,0 -> 3,3 : 6
0,0 -> 2,4 : 6
0,0 -> 4,2 : 6

minHeap


"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minHeap = [(0,points[0][0],points[0][1])] #dist, x , y
        res = 0
        visit = set()

        while len(visit) < len(points):

            dist, x, y = heapq.heappop(minHeap)

            if (x,y) in visit:
                continue
            
            res += dist
            visit.add((x,y))

            for x1, y1 in points:
                heapq.heappush(minHeap, (abs(x-x1) + abs(y-y1), x1, y1))
        
        return res
        
