"""

[2,,2,2]

1



"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)

            if abs(x) > abs(y):
                z = abs(x) - abs(y)
                heapq.heappush(maxHeap, -1 * z)
        
        if maxHeap:
            return -1 * maxHeap[0]
        else:
            return 0