"""
[1,2,4,2,3,5,3,4]

4

{
    1 : 0
    2 : 0
    3 : 0
    4 : 1
    5 : 1
}

[1,2,3,3,4,5,6,7]



min_heap = []

make sure if the val is 0 pop out of heap
"""

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        
        freq_map = defaultdict(int)
        for h in hand:
            freq_map[h] += 1
        
        minHeap = []
        for key in freq_map.keys():
            heapq.heappush(minHeap, key)
        
        while minHeap:

            start = minHeap[0]

            group = 0

            while group < groupSize:

                if start not in freq_map:
                    return False

                freq_map[start] -= 1

                if freq_map[start] == 0:

                    if minHeap[0] != start:
                        return False

                    heapq.heappop(minHeap)

                start += 1
                group += 1

        return True