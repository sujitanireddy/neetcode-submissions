"""
[[0,2],[2,2]] k=1

minHeap = [(dist,x,y)]



"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        res = []

        for x, y in points:
            dist = abs((x - 0) ** 2 + (y - 0) ** 2)
            heapq.heappush(minHeap, (dist, x, y))
        
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        
        return res