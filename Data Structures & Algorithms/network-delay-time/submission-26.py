class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        minHeap = [(0, k)] #(time, node)
        visit = set()
        min_time = 0
        adjList = defaultdict(list)
        
        for u,v,t in times:
            adjList[u].append((t, v))
        
        while minHeap:
            
            time, node = heapq.heappop(minHeap)
            
            if node in visit:
                continue
            
            visit.add(node)
            min_time = time
            
            for t1, n1 in adjList[node]:
                heapq.heappush(minHeap, (t1 + time, n1))

        if len(visit) == n:
            return min_time
        else:
            return -1