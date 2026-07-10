class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        """
        [[0,2],[2,2]], k = 1

        - Iterate over points. Calculate distace
        - min_heap = [(-d,x,y)]

        """

        min_heap = []
        output = []

        for x, y in points:
            d = (((0 - x) ** 2) + ((0 - y) ** 2))
            heapq.heappush(min_heap, (d, x, y))
        
        while len(output) < k:
            d, x, y = heapq.heappop(min_heap)
            output.append([x,y])

        return output