class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)

        maxheap = []
        for cnt in freq.values():
            maxheap.append(-cnt)

        heapq.heapify(maxheap)

        q = deque() #(cnt, cooldown_time)
        time = 0

        while maxheap or q:
            time += 1

            if not maxheap:
                time = q[0][1]
            
            else:
                cnt = 1 + heapq.heappop(maxheap)

                if cnt:
                    q.append((cnt, time + n))
            
            if q and time == q[0][1]:
                heapq.heappush(maxheap, q.popleft()[0])
        
        return time
            


