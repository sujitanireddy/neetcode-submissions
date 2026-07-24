"""
- We make sure the diff in lenght between the self.max_heap and self.min_heap is not greater than 1.
- We compare the max from self.max_heap and min from self.min_heap and move elements as necessary.
"""

class MedianFinder:

    def __init__(self):
        self.max_heap = [] #First half values 
        self.min_heap = [] #Second half values

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, num * -1)
        
        if self.max_heap and self.min_heap and (self.max_heap[0] * -1) > self.min_heap[0]:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val * -1)

        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val * -1)

        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, val * -1)

    def findMedian(self) -> float:

        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        
        else:
            return ((-1 * self.max_heap[0]) + self.min_heap[0]) / 2
        
        