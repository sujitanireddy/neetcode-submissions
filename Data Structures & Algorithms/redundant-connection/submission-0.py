class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        
        #check if graph is still connected and has no cycles
        def dfs(adjList, node,visit):

            visit.add(node)

            for nei in adjList[node]:
                if nei not in visit:
                    dfs(adjList, nei,visit)

        
        def build_adjlist(skp_index):
            adjList = defaultdict(list)
            visit = set()

            for i, (u,v) in enumerate(edges):
                if skp_index == i:
                    continue
                adjList[u].append(v)
                adjList[v].append(u)
            
            dfs(adjList, 1, visit)
            return len(visit) == n
        

        for i in range(n-1,-1,-1):
            if build_adjlist(i):
                return edges[i]