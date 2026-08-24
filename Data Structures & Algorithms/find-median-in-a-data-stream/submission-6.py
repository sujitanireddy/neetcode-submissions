"""
BruteForce:
- [1,3,2] = O(1)
- findmedian = n * O(nlogn)

Optimal:
- [5,6]     [7,8,9]

push : logn
findmedian : logn

Can we maintain the sorted property while adding a num without actually sorting? 
left array last element > right array last element and left half < right half

self.maxHeap = leftarray
self.minHeap = rightarray

self.maxHeap      self.minHeap
[-1]           [2,3]

- The diff in lenghts of max and min heap < 2
- if self.maxHeap[0] > self.minHeap[0]: move the no over to self.minHeap

"""
class MedianFinder:

    def __init__(self):
        self.maxHeap = [] #left values
        self.minHeap = [] #right values

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.maxHeap, num * -1)

        if self.maxHeap and self.minHeap and -1 * self.maxHeap[0] >= self.minHeap[0]:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

        if self.maxHeap and self.minHeap and self.minHeap[0] <= -1 * self.maxHeap[0]:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val * -1)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val * -1)


    def findMedian(self) -> float:

        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        
        else:
            return (self.minHeap[0] + (self.maxHeap[0] * -1)) / 2





















        
        