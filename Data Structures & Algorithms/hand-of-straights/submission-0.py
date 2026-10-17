"""
[1,2,4,2,3,5,3,4]
if len(hand) % 4 != 0:
    return False

are we puching a hole in the array so that another gourp is not possible??

"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False
        
        freq_map = defaultdict(int)
        for val in hand:
            freq_map[val] += 1
        
        minHeap = list(freq_map.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first+groupSize):

                if i not in freq_map:
                    return False
                
                freq_map[i] -= 1

                if freq_map[i] == 0:

                    if minHeap[0] != i:
                        return False

                    heapq.heappop(minHeap)

        return True