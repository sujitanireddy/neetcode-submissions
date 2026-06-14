class MedianFinder:

    def __init__(self):
        self.small = [] #max_heap
        self.large = [] #min_heap

    def addNum(self, num: int) -> None:

        heapq.heappush(self.small, -1 * num)

        if (self.small and self.large and (self.small[0] * -1) > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        
        #uneven sizes
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            val = -1 * self.small[0]
            return val
        
        elif len(self.large) > len(self.small):
            val = self.large[0]
            return val
        
        else:
            return ((self.small[0] * -1) + self.large[0]) / 2
            