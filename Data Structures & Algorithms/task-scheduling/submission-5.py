class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # hashmap -> O(n)
        # max freq -> max_heap O(1)
        # queue -> pop and pusing is O(1)

        freq_map = Counter(tasks)
        max_heap = [-n for n in freq_map.values()]
        heapq.heapify(max_heap)
        q = deque() #[(cnt, releasetime)]
        time = 0
        

        while max_heap or q:

            time += 1

            if not max_heap:
                time = q[0][1]

            else:
                cnt = 1 + heapq.heappop(max_heap)

                if cnt:
                    q.append((cnt, n + time))

            if q and time == q[0][1]:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return time