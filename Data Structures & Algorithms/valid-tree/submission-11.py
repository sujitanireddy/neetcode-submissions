class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        if not edges: return True

        if len(edges) >= n:
            return False

        No cycles, all the nodes are connected.

        - add both edges to the dict key while traversing
        - visit set

        {
            0 : [1,2,3]
            1 : [0, 4]
            2 : [0]
            3 : [0]
            4 : [1]
        }
        """
        if not edges: return True

        if len(edges) >= n: return False

        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()

        def dfs(n):

            visit.add(n)

            for nei in adjList[n]:
                if nei not in visit:
                    dfs(nei)
        
        dfs(0)

        if len(visit) == n:
            return True
        
        return False
