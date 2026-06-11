class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        
        for x,y in points:
            distance = ((0 - x) ** 2) + ((0 - y) ** 2)
            heapq.heappush(min_heap, [distance, x, y])
        
        output = []
        for i in range(k):
            distance, x, y = heapq.heappop(min_heap)
            output.append([x,y])
        
        return output


