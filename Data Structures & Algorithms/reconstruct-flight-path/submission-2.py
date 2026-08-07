class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        res = []
        adjList = defaultdict(list)
        for src, des in tickets:
            heapq.heappush(adjList[src], des)

        def dfs(airport):

            while adjList[airport]:
                next_airport = heapq.heappop(adjList[airport])
                dfs(next_airport)

            res.append(airport)


        dfs("JFK")

        return res[::-1]