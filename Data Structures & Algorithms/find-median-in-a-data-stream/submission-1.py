class MedianFinder:

    def __init__(self):
        self.max_heap = [] #stores smaller half of the values
        self.min_heap = [] # min_heap >= max_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -1 * num)

        #maintain min and max heap properties
        if (self.max_heap and self.min_heap and (self.max_heap[0] * -1) > self.min_heap[0]):
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        #handle uneven lengths
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -1 * heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1 * val)
        
        print(self.max_heap)
        print(self.min_heap)

    def findMedian(self) -> float:
        
        if len(self.max_heap) > len(self.min_heap):
            return -1 * self.max_heap[0]
        
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]

        else:
            return (((-1 * self.max_heap[0]) + self.min_heap[0]) / 2)
        