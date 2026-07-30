class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visit = set()
        
        adjList = defaultdict(list)
        for src, des in edges:
            adjList[src].append(des)
            adjList[des].append(src)

        def dfs(node, prevNode):

            if node in visit:
                return False
            
            visit.add(node)

            for n in adjList[node]:
                if prevNode == n:
                    continue
                if not dfs(n, node):
                    return False
            
            return True

        
        return dfs(0,-1) and len(visit) == n

