"""
adjList = Graph Graph
{
   1 : [2,4]
   2 : [3]
   3 : [4]
}
  s d t
[[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

    1      1
1 ----> 2 ---> 3 
|              |
|4             |
|             1|
4<-------------

- Dijstra's
- visit all the nodes in the graph with the min time

minHeap = [(4,4)(4,3)]
while minHeap:

visit = (1,2)

time taken = 3

TC: V log E
SC: O(E)
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = {i:[] for i in range(1,n+1)}
        for s, d, t in times:
            adjList[s].append((t,d)) #s : [(t,d)]
        
        minHeap = [(0,k)] #time, node
        visit = set()
        mintime = 0

        while minHeap:

            time, node = heapq.heappop(minHeap)

            if node in visit:
                continue
            
            visit.add(node)
            mintime = time

            if len(visit) == n:
                return mintime

            for t1, n1 in adjList[node]:
                if n1 not in visit:
                    heapq.heappush(minHeap, (t1+time, n1))

        return -1 


















