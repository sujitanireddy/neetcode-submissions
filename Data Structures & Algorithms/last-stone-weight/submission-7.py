class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]

        heapq.heapify(stones)

        while len(stones) > 1:

            stone_A = -1 * heapq.heappop(stones)
            stone_B = -1 * heapq.heappop(stones)

            print(stone_A)
            print(stone_B)

            if stone_A != stone_B:
                stones.append(-1 * abs(stone_A - stone_B))
        
        stones.append(0)
        
        return -1 * stones[0]


