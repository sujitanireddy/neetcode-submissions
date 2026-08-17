"""
src = JFK

if multiple flights: first visit smallest one

Graph Rep: AdjList 

{
  BUF : [HOU]
  HOU : [SEA]
  JFK : [BUF]
}

JFK -> BUF -> HOU -> SEA
[["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

{
   HOU : []
   SEA : []
   JFK : [] (minheap)
}

[JFK,HOU,JFK,

JFK -> HOU -> JFK -> SEA -> JFK

base case: if not adjList[airport]: return

res array

TC: O(V+E)
SC: O(n)

["JFK", "HOU", "JFK", "SEA", "JFK" ]

[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

{
  JFK : [NRT]
  NRT : [JFK]
}

["JFK","KUL",]

"""

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        res = []
        adjList = defaultdict(list)
        
        for src, des in tickets:
            heapq.heappush(adjList[src], des)

        def dfs(airport):

            if not adjList[airport]:
                res.append(airport)
                return

            while adjList[airport]:
                new_airport = heapq.heappop(adjList[airport])
                dfs(new_airport)

            res.append(airport)

        dfs("JFK")

        return res[::-1]


