class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        """
        Complete Graph

        minHeap = [] #cost, idx

        output += 0

        double loop to get all costs into the minHeap        
        """
        minHeap = [(0,0)] #cost, index
        res = 0
        visit = set()
        n = len(points)

        while len(visit) < len(points):

            cost, i = heapq.heappop(minHeap)

            x, y = points[i]

            if (x,y) in visit:
                continue

            visit.add((x,y))
            res += cost

            for j in range(n):
                dis = abs(x - points[j][0]) + abs(y - points[j][1])
                heapq.heappush(minHeap, (dis, j))

        return res