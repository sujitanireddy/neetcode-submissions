class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        """
        max_heap = O(1), heapify O(n), heappush = log(n)
        
        """

        if not stones:
            return 0

        max_heap = []
        
        for i in range(len(stones)):
            heapq.heappush(max_heap, stones[i] * -1)

        while len(max_heap) > 1:

            max1 = -1 * heapq.heappop(max_heap)
            max2 = -1 * heapq.heappop(max_heap)

            if max1 > max2:
                heapq.heappush(max_heap, -1 * (max1 - max2))
        
        if max_heap:
            return -1 * max_heap[0]
        else:
            return 0
