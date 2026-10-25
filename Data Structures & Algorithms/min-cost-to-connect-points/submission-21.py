"""

Calculate MST of a complete graph


"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        minHeap = [(0, points[0][0], points[0][1])] #(dist, x, y)
        visit = set()
        res = 0

        while len(visit) < len(points):

            dist, x, y = heapq.heappop(minHeap)

            if (x,y) in visit:
                continue

            res += dist
            visit.add((x,y))

            for x1, y1 in points:
                manhattan_distance = abs(x-x1) + abs(y-y1)
                if (x1,y1) in visit:
                    continue
                heapq.heappush(minHeap, (manhattan_distance, x1, y1))

        return res