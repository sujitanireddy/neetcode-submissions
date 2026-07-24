"""
X -> Y -> I -> X -> Y

max_heap = [()]

- Use a hashamp to count freq {Task : freq}
- Push the feq into the max_heap [(-freq)]
- Queue to keep track of tasks when the cooldown is completed.

{A : 3
B : 1
C : 1}

max_heap = []



q = []

cycles = 4

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        cycles = 0
        q = deque() #(cooldown, freq)
        
        task_freq_map = defaultdict(int)
        for task in tasks:
            task_freq_map[task] += 1
        
        max_heap = []
        for freq in task_freq_map.values():
            heapq.heappush(max_heap, -1 * freq)
        
        while max_heap or q:

            if not max_heap:
                cycles = q[0][0]
            
            else:
                freq = heapq.heappop(max_heap) * -1
                freq -= 1
                cycles += 1

                if freq > 0:
                    q.append((cycles + n, freq))


            if q and q[0][0] == cycles:
                cooldown, remaining_freq = q.popleft()
                heapq.heappush(max_heap, remaining_freq * -1)

        return cycles












