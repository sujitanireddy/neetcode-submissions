class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        """
        Adjlist
        {
          0 : [1]
          1 : [0, 2]
          2 : [1]
          3 : [4]
          4 : [3]        
        }

        dfs
        - if we already visited then there is a cycle. Stop looping

        v = {0,1,2,3,4}

        """

        adjList = defaultdict(list)
        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()
        graphs = 0

        def dfs(node):

            visit.add(node)

            for nei in adjList[node]:
                if nei not in visit:
                    dfs(nei)

        for i in range(n):
            if i not in visit:
                dfs(i)
                graphs += 1
        
        return graphs