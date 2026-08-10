class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        TC: O(v + E) Considering n is unique vertices
        SC: O(v + E) 

        {
            #src: [des (sorted)] #heap
            HOU : []
            SEA : []
            JFK : []
        }

        [JFK, HOU, JFK, SEA, JFK]

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
