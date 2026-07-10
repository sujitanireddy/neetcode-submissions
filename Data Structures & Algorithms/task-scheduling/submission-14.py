class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        """
        "X","X","Y","Y"         n = 2

        X -> Y -> idel -> X -> Y = 5

        "A","A","A","B","C"      n = 3

        A -> B -> C -> idel -> A -> idel -> idel -> idel -> A = 9

        Observations
        - Start with task with maximum freq

        DS:
        hashmap = {task: freq}
        max_heap = [(-freq, char)]
        queue = [(cooldown_time)]

        """
        freq_map = defaultdict(int)
        for task in tasks:
            freq_map[task] += 1
        
        max_heap = []
        for freq in freq_map.values():
            heapq.heappush(max_heap, -freq)
        
        cycles = 0
        q = deque()

        while max_heap or q:

            if not max_heap:
                cycles = q[0][1]
            
            else:
                cycles += 1
                freq = (-1 * heapq.heappop(max_heap)) - 1

                if freq > 0:
                    cooldown = cycles + n
                    q.append((freq, cooldown))

            if q and q[0][1] == cycles:
                freq, cooldown = q.popleft()
                heapq.heappush(max_heap, -freq)

        return cycles


