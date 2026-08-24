class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        {
          HOU : JFK
          SEA : JFK 
          JFK : SEA,HOU
        }

        """
        
        adjList = defaultdict(list)
        for src, des in tickets:
            heapq.heappush(adjList[src], des)

        res = []
        
        def dfs(airport):
            
            while adjList[airport]:
                popped_airport = heapq.heappop(adjList[airport])
                dfs(popped_airport)
            
            res.append(airport)

        dfs("JFK")
        return res[::-1]