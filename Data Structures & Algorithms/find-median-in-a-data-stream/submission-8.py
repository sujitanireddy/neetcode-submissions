"""
Notes:

1   2   3   4

1   2   3



Two Heaps

max_heap            min_heap
[1]                  [7]    


Notes:
- if the diff b/w the heaps is greater than 1 then move them
- max_heap for first half of smaller values of the array nad min_heap for second half of bigger values of the array
- 

"""
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.maxHeap, num * -1)

        if self.maxHeap and self.minHeap and -1 * self.maxHeap[0] > self.minHeap[0]:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val * -1)

    def findMedian(self) -> float:

        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        else:
            return (self.minHeap[0] + -1 * self.maxHeap[0]) / 2 
        
        