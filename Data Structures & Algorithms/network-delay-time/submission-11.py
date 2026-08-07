class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        """
        { 
          1 : (2,1), (4,4)
          2 : (3,1)
          3 : (4,1)
        }

        """

        adjList = defaultdict(list)
        for u,v,t in times:
            adjList[u].append((v,t))

        min_heap = [(0, k)] #time, node
        time = 0
        visit = set()

        while min_heap:

            t1, n1 = heapq.heappop(min_heap)

            if n1 in visit:
                continue

            time = t1
            visit.add(n1)

            for n2, t2 in adjList[n1]:

                if n2 not in visit:

                    heapq.heappush(min_heap, (t1 + t2, n2))
        
        print(visit)

        if len(visit) == n:
            return time
        
        return -1





