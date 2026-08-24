class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = {task : 0 for task in tasks}
        for task in tasks:
            freq[task] += 1

        maxHeap = []
        q = deque() #(cooldown, freq)

        for freq in freq.values():
            heapq.heappush(maxHeap, -1 * freq)
        
        #[]
        #(4,2)
        #q = []
        time = 0
        while maxHeap or q:

            if not maxHeap:
                time = q[0][0]
            
            else:

                time += 1 #time = 4

                remiaining_freq = (heapq.heappop(maxHeap) * -1) - 1

                if remiaining_freq > 0:
                    q.append((time+n, remiaining_freq))
                
            if q and time == q[0][0]:
                cooldown, freq = q.popleft()
                heapq.heappush(maxHeap, freq * -1 )

        return time
