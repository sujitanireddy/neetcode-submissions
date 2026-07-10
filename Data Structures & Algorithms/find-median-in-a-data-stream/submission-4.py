class MedianFinder:

    """
    dynamic array = [1] sort and get median =  n * O(nlogn)

    Median is the middle most element. 

    max_heap(-ve values)        min_heap
    [-1,-2]                          [3]

    - default adding any number to max_heap. 
        - Validate if that number is a good fit in maxheap. 
            - if max_heap[0] < min_heap[0] then it's good

    - Always keep the diffrence of lenghts <= 1 
    """

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        
    def addNum(self, num: int) -> None:

        heapq.heappush(self.maxheap, (-1 * num))

        print(self.maxheap)
 
        if self.maxheap and self.minheap and (-1 * self.maxheap[0]) > self.minheap[0]:
            val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)

        if len(self.minheap) > len(self.maxheap) + 1:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1 * val)

        if len(self.maxheap) > len(self.minheap) + 1:
            val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)
        
        print(self.maxheap)
        print(self.minheap)

    def findMedian(self) -> float:

        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        
        elif len(self.maxheap) < len(self.minheap):
            return self.minheap[0]
        
        else:
            return (((-1 * self.maxheap[0]) + (self.minheap[0])) / 2)
        
        