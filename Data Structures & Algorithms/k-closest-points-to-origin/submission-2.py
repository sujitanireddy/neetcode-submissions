class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        min_heap = []

        for x, y in points:
            distance = (0 - x)**2 + (0 - y)**2
            min_heap.append([distance, x, y])

        heapq.heapify(min_heap)
        
        output = []
        counter = 0
        while counter < k:
            distance, x, y = heapq.heappop(min_heap)
            output.append([x,y])
            counter += 1
        
        return output
