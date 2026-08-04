class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        """
        Valid Tree: No cylces, all nodes are connected

        E = (V - 1) (use this to return early). If all nodes are connected then it's a tree

        {
            0 : [1]
            1 : [0,2,3,4]
            2 : [1,3]
            3 : [2,1]
            4 : [1]
        }

        """
        if len(edges) >= n:
            return False

        visit = set()
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        def dfs(n):
            
            visit.add(n)

            for nei in adjList[n]:
                if nei not in visit:
                    dfs(nei)


        dfs(0)

        return len(visit) == n and (n - 1) == len(edges)