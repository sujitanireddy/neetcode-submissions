class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        """
        This is a complete graph. Have to compute cost from one point to every other point.
              4
        [0,0] - [2,2]
         | 6 
        [3,3]

        visit = {}
        """

        n = len(points)
        total_cost = 0
        visit = set()
        minHeap = [(0,0)] #cost, index

        while len(visit) < n:

            cost, i = heapq.heappop(minHeap)

            x, y = points[i]

            if (x,y) in visit:
                continue

            total_cost += cost
            visit.add((x,y))

            for j in range(n):
                dis = abs(x - points[j][0]) + abs( y - points[j][1])
                heapq.heappush(minHeap, (dis, j))
        
        return total_cost
