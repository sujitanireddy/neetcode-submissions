class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #hashmap - Calculate the freq of tasks [3,1,1]
        #heap - retrive the max tasks
        #queue - holds the tasks and waittime

        #waittime - the time that the task has to wait until it is it's turn
        #cycles

        char_freq_map = Counter(tasks)
        max_heap = [-c for c in char_freq_map.values()] #[-freq]
        heapq.heapify(max_heap) 
        q = deque() #[(freq_remaining, waittime)]
        cycles = 0

        #max_heap = []
        #q = []
        #cycles = 5
        
        while max_heap or q:

            cycles += 1

            if not max_heap:
                cycles = q[0][1]
            
            else:
                freq = 1 + heapq.heappop(max_heap)

                if freq < 0:
                    q.append((freq, cycles + n))

            if q and q[0][1] == cycles:
                freq_remaining, waittime = q.popleft()
                heapq.heappush(max_heap, freq_remaining)


        return cycles














