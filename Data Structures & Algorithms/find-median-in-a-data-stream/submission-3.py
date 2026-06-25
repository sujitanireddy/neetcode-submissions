#2 heap.    max_heap[]    min_heap[]
#property max_heap[0] <= min_heap[0]
#len is not greater than one

class MedianFinder:

    def __init__(self):
        self.small = [] #max_heap
        self.large = [] #min_heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #uneven lengths
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float: #O(nlongn) * n
        
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        else:
            return ((-1 * self.small[0] + self.large[0]) / 2)