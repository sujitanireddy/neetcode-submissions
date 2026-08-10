class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        {
            1 : [(1,2), (4,4)] #src: [(time, des)]
            2 : [(1,3)]
            3 : [(1,4)]
        }
        minHeap = [(4,4)] #time, node
        popped minHeap
        (0,1)
        (1,2)
        (1,3)
        (1,4)
        time = 3
        """
        visit = set()
        minHeap = [(0,k)] #time, node
        res = 0
        adjList = defaultdict(list)

        for src, des, time in times:
            adjList[src].append((time, des))
        
        while minHeap:

            time, node = heapq.heappop(minHeap)
            
            if node in visit:
                continue

            visit.add(node)
            res = time

            if len(visit) == n:
                return res
            
            for t, des in adjList[node]:
                if des not in visit:
                    heapq.heappush(minHeap, (time + t, des))
        
        return -1
                