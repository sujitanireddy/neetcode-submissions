class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adjList = defaultdict(list) #src : [(cost,x,y)] x,y are the des cords

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adjList[tuple(points[i])].append((distance, points[j][0], points[j][1]))
                adjList[tuple(points[j])].append((distance, points[i][0], points[i][1]))

        res = 0
        total_no_of_vertices = len(points)
        visit = set()
        minHeap = []
        minHeap.append((0, points[0][0], points[0][1])) #cost, x, y

        while len(visit) != total_no_of_vertices:
            
            cost, x, y = heapq.heappop(minHeap)

            if (x, y) in visit:
                continue

            res += cost
            visit.add((x,y))

            for nei in adjList[(x,y)]:

                if (nei[1], nei[2]) not in visit:

                    heapq.heappush(minHeap, (nei[0], nei[1], nei[2]))

        return res

