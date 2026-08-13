class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        """
        {
            1 : [(1,2), (4,4)] #src : (w, des)
            2 : [(1,3)]
            3 : [(1,4)]
        }
        minHeap = [(4,4),] #w, node
        t = 3
        (3,4)
        visit = {1,2,3,4}

        """
        adjList = { i :[] for i in range(1, n+1)}

        for src, des, w in times:
            adjList[src].append((w, des))
        
        minHeap = [(0,k)] #w,node
        visit = set()
        res = 0

        while minHeap:

            time, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            
            visit.add(node)
            res = time

            if len(visit) == n:
                return res

            for w, des in adjList[node]:
                if des not in visit:
                    heapq.heappush(minHeap, (w + time, des))
        
        return -1
