"""
src: "JFK"

notes:
- each ticket is used once
- lexical order

[["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]

{
    BUF: HOU
    HOU: SEA
    JFK: BUF
}
[JFK,BUF,HOU,SEA]

[["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]

{
    HOU: []
    SEA: [JFK]
    JFK: [ ] #heap
}
airport next_airport
JFK - HOU
HOU - JFK
JFK - SEA
SEA - JFK
JFK

[JFK - SEA - JFK - HOU - JFK]

JFK - HOU - JFK - SEA - JFK

Algo:
- DFS
- Capture the airport while backtracking

Return the res reversed.

"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        res = []
        
        #build adjList
        adjList = defaultdict(list)
        for src, des in tickets:
            heapq.heappush(adjList[src], des)

        print(adjList)
        
        def dfs(airport):

            while adjList[airport]:

                for nei in adjList[airport]:
                    next_airport = heapq.heappop(adjList[airport])
                    dfs(next_airport)
                
            res.append(airport)

        dfs("JFK")
        return res[::-1]







































