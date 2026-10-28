"""
tasks = ["A","A","A","B","C"], n = 3

max_heap = ()

task_freq = 2

q = [(4,2), ]

cycles = 3

when max_heap is empty and we still did not reach cycles, simply make cycles == q[0][0]

"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        task_freq_map = defaultdict(int)
        for task in tasks:
            task_freq_map[task] += 1
        
        maxHeap = [] #(-freq_tasks)
        for freq in task_freq_map.values():
            maxHeap.append(-freq)
        
        heapq.heapify(maxHeap)

        q = deque() #(cooldown_time, remaining_tasks)
        cycles = 0

        while q or maxHeap:

            if not maxHeap:
                cycles = q[0][0]

            if maxHeap:
                task_freq = -1 * heapq.heappop(maxHeap)
                task_freq -= 1
                cycles += 1
                
                if task_freq > 0:
                    cooldown = n + cycles
                    q.append((cooldown, task_freq))
                
            if q and q[0][0] == cycles:
                time, remaining_freq = q.popleft()
                heapq.heappush(maxHeap, remaining_freq * -1)
            
        return cycles
            
                
            



