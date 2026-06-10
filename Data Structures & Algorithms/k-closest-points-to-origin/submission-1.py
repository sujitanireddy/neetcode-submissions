class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #sqrt((x1 - x2)^2 + (y1 - y2)^2))

        heap = []

        for point in points:
            distance = (0 - point[0])**2 + (0 - point[1])**2
            heap.append([distance, point])

        heapq.heapify(heap)
        
        output = []
        counter = 0
        while counter < k:
            distance, point = heapq.heappop(heap)
            output.append(point)
            counter += 1
        
        return output
