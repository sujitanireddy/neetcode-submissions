"""
[4,2,5,3]

1,2,3,4 
2,3,4,5

hashmap
minheap

[1,2,3,3,4,5,6,7], groupSize = 4

{
    1: 0
    2: 0
    3: 0
    4: 0
    5: 1
    6: 1
    7: 1
}

[5,6,7]
from 1 - 4

"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        val_freq_map = defaultdict(int)
        for c in hand:
            val_freq_map[c] += 1

        minHeap = []
        for key in val_freq_map.keys():
            minHeap.append(key)

        heapq.heapify(minHeap)

        while minHeap:

            val = minHeap[0]

            for i in range(val, val+groupSize):

                if i not in val_freq_map:
                    return False

                val_freq_map[i] -= 1

                if val_freq_map[i] == 0:
                    if minHeap[0] != i:
                        return False
                    heapq.heappop(minHeap)
        
        return True















