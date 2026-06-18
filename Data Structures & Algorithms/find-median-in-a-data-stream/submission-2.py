class MedianFinder:

    """
    small(max_heap)         large(min_heap)
    [-1,-2]                      [3]
    """

    def __init__(self):
        self.small = [] #max_heap
        self.large = [] #min_heap 

    def addNum(self, num: int) -> None:
        
        #append to the small heap
        heapq.heappush(self.small, -1 * num)

        #check if the newly appended value belongs in the small heap, if not move to large heap
        if self.small and self.large and -1 * self.small[0] > self.large[0]:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        #handle uneven lengths
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        else:
            return ((self.small[0] * -1 + self.large[0])/2)
    