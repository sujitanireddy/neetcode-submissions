"""
Algo:
- Dijsktras

DS:
- minHeap
- Hashmap for adjList

Adjlist format
{
    1 : [(4,4), (2,1)] #src : [(des, time)]
}

minHeap format:
[(time,node)]
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = {i :[] for i in range(1, n+1)}

        for src,des,time in times:
            adjList[src].append((des,time))
        
        minHeap = [(0,k)]
        visit = set()
        res = 0

        while minHeap:

            t1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            res = t1

            if len(visit) == n:
                return res

            for n2,t2 in adjList[n1]:
                heapq.heappush(minHeap, (t1 + t2, n2))
        
        return -1