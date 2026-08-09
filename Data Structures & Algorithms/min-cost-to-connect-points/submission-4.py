class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        res = 0
        total_no_of_vertices = len(points)
        visit = set()
        minHeap = []
        minHeap.append((0,0)) #cost, idx

        while len(visit) < total_no_of_vertices:
            
            cost, i = heapq.heappop(minHeap)

            if i in visit:
                continue

            res += cost
            visit.add(i)

            x, y = points[i]

            for j in range(n):
                dist = abs(x - points[j][0]) + abs(y - points[j][1])
                heapq.heappush(minHeap, (dist, j))

        return res

