class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Observations: A parent can have multiple children, but children cannot have multiple parents.

        When I am doing my recursive DFS.

        If we encounter the visited node again, then we can return False. There is a cycle in the graph.
        """

        adjList = defaultdict(list)
        for parent, child in edges:
            adjList[parent].append(child)
            adjList[child].append(parent)

        visit = set()

        def dfs(node, prev):

            if node in visit:
                return False

            visit.add(node)

            for p in adjList[node]:
                if p == prev:
                    continue
                if not dfs(p, node):
                    return False

            return True
        
        return dfs(0,-1) and len(visit) == n
