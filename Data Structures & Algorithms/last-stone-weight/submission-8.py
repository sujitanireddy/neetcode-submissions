class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            big_stone = -1 * heapq.heappop(stones)
            small_stone = -1 * heapq.heappop(stones)

            if big_stone != small_stone:
                heapq.heappush(stones, (-1 * (big_stone - small_stone)))
        
        stones.append(0)

        return -1 * stones[0]