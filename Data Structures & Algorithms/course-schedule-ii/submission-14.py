class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = {i : [] for i in range(numCourses)}
        for u, v in prerequisites:
            adjList[u].append(v)
        
        visit = set()
        processed = set()
        res = []

        def dfs(c):
            
            if c in processed:
                return True
            
            if c in visit:
                return False
            
            visit.add(c)

            for nei in adjList[c]:
                if not dfs(nei):
                    return False
            
            visit.remove(c)
            processed.add(c)
            res.append(c)

            return True

        for c in range(numCourses):
            if c not in processed:
                if not dfs(c):
                    return []
        
        return res