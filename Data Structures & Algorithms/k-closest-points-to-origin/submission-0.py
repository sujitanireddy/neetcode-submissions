class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #sqrt((x1 - x2)^2 + (y1 - y2)^2))

        heap = []

        for point in points:
            distance = math.sqrt((0 - point[0])**2 + (0 - point[1])**2)
            heapq.heappush(heap, (distance, point))
        
        output = []
        counter = 0
        while counter < k:
            distance, point = heapq.heappop(heap)
            output.append(point)
            counter += 1
        
        return output
