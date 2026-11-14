"""
lexigraphically -> A -> B

Example 1:
[["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]

{
    BUF: HOU
    HOU: SEA
    JFK: BUF
}

JFK -> BUF -> HOU -> SEA

Example 2:

[["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

{
    HOU: JFK
    SEA: JFK
    JFK: []
}

JFK -> HOU -> JFK -> SEA -> JFK

- minHeap in adjList values to maintain lexographically odering.

TC: O(V+E)
SC: O(V+E)

"""
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


#Unit testing
"""

{
    HOU: []
    SEA: []
    JFK: []
}

res = [JFK, SEA]




"""


        