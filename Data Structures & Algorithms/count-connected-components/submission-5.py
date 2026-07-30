class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graphs = 0
        visit = set()
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(node):

            visit.add(node)

            for c in adjList[node]:
                if c not in visit:
                    dfs(c)


        for i in range(n):
            if i not in visit:
                dfs(i)
                graphs += 1
        
        return graphs