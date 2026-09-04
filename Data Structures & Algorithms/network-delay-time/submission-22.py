"""
Dijstkra's

minHeap = [(1,2), (4,4)] #(time, des)
visit = {1}

adjList # src : [(time, des)]
{
    1 : [(2,1),(4,4)]
    2 : [(3,1)]
    3 : [(4,1)]
}

t = 0
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        minHeap = [(0,k)] #(time, des)
        visit = set() #visited nodes
        adjList = defaultdict(list) #src : [(time, des)]

        for u, v, t in times:
            adjList[u].append((t,v))
        
        while minHeap:

            t1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            
            visit.add(n1)
            res = t1

            if len(visit) == n:
                return res

            for t2, n2 in adjList[n1]:
                heapq.heappush(minHeap, (t2+t1, n2))
        
        return -1