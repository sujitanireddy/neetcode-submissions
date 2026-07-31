class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        To be a tree: No cycles and all the vertices are connected.

        if n >= len(edges): return False

        { 
          0 : [1,2,3]
          1 : [0,4]
          2 : [0]
          3 : [0]
          4 : [1]  
        }

        dfs(node, prevNode) = if we visit the same node again, we can conclude that there is a cycle
        if it's prevNode then skip

        if len(visit) == n

        visit = {0,1,4}
        """
        if n <= len(edges):
            return False

        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        visit = set()
        
        def dfs(node,prevNode):

            if node in visit:
                return False
            
            visit.add(node)

            for nei in adjList[node]:
                if prevNode == nei:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0,-1) and len(visit) == n
        