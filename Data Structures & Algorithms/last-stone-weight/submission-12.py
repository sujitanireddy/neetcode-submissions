class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        #Algorithm
        #Convert stones to a maxheap
        #heapify
        #At every step -> heahpop the two largest values 
            #compute
            #heappush
        #When length is either 0 or 1. Return

        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:

            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                z = y - x
                heapq.heappush(stones, -z)

        stones.append(0)
        
        return abs(stones[0])
            

