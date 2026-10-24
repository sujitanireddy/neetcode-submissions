class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        num_freq_map = defaultdict(int)
        for n in hand:
            num_freq_map[n] += 1
        
        minHeap = []
        for key in num_freq_map.keys():
            minHeap.append(key)
        
        heapq.heapify(minHeap)

        while minHeap:

            val = minHeap[0]

            for i in range(val, val + groupSize):

                if i not in num_freq_map:
                    return False

                num_freq_map[i] -= 1

                if num_freq_map[i] == 0:

                    if minHeap[0] != i:
                        return False
                    
                    heapq.heappop(minHeap)
        
        return True
            

