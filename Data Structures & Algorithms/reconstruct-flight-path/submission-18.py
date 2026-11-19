class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for src, des in tickets:
            heapq.heappush(adjList[src], des)

        res = []
        
        def dfs(airport):
            
            while adjList[airport]:
                new_airport = heapq.heappop(adjList[airport])
                dfs(new_airport)
            
            res.append(airport)

        dfs("JFK")
        return res[::-1]