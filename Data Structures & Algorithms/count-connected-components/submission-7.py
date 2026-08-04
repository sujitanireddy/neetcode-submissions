class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        """
        {0 1 2} {3 4}

        """
        graphs = 0
        visit = set()
        adjList = defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(n):

            visit.add(n)

            for nei in adjList[n]:
                if nei not in visit:
                    dfs(nei)

        for i in range(n):
            if i not in visit:
                dfs(i)
                graphs += 1

        return graphs