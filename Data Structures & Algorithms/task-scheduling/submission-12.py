class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq_map = defaultdict(int)

        for task in tasks:
            freq_map[task] += 1
        
        max_heap = [-n for n in freq_map.values()]
        heapq.heapify(max_heap)
        q = deque()

        cycles = 0
        while max_heap or q:

            if not max_heap:
                cycles = q[0][1]

            else:
                cycles += 1
                freq = (-1 * heapq.heappop(max_heap)) - 1
                
                if freq > 0:
                    q.append((freq, cycles + n))
            
            while q and cycles == q[0][1]:
                freq, time = q.popleft()
                heapq.heappush(max_heap, -freq)
        
        return cycles
        
