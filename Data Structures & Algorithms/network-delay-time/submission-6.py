class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = defaultdict(list)
        
        #src : [(des, time)
        for u, v, t in times:
            adjList[u].append((v,t))

        #(time, node)
        minheap = [(0, k)]
        visit = set()

        time_taken = float("-inf")

        while minheap:

            t1, n1 = heapq.heappop(minheap)

            if n1 in visit:
                continue
            
            time_taken = t1 
            visit.add(n1)

            for n2, t2 in adjList[n1]:

                if n2 not in visit:
                    heapq.heappush(minheap, (t1+t2, n2))
        
        if len(visit) != n:
            return -1 
        
        return time_taken



