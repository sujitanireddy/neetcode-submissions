class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #tasks = ["X","X","Y","Y"].  n = 2
        # X -> Y -> idle -> X -> Y 
        # 1(X,4), 2(Y,5)
        # tasks = ["A","A","A","B","C"], n = 3
        # A B C - A - - - A
        #calculate the freq of each task (hashamp) (O(n))
        #Start with the max freq task heap(max) O(1), O(logn)
            #if the task has more cycles to be performed until fully exhausted then store them seperatly (queue) (O(1), O(1))
        #whenever the cycles count reach this stored time of tasks then use them again
        
        freq_map = Counter(tasks)
        max_heap = [-n for n in freq_map.values()]
        heapq.heapify(max_heap) #O(n)
        q = deque() #[(freq, cooldown_time)]
        cycles = 0

        while max_heap or q:
            
            cycles += 1

            if not max_heap:
                cycles = q[0][1]

            else:
                freq = heapq.heappop(max_heap) + 1

                if freq < 0:
                    q.append((freq, (cycles + n)))

            if q and q[0][1] == cycles:
                freq, cooldown = q.popleft()
                heapq.heappush(max_heap, freq)

        return cycles
            




