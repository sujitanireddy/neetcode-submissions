class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] *= -1
        
        heapq.heapify(stones)

        while len(stones) > 1:

            stone_a = -1 * heapq.heappop(stones)
            stone_b = -1 * heapq.heappop(stones)

            heapq.heappush(stones, -1 * (stone_a - stone_b))

        return -1 * stones[0]