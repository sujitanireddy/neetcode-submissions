class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)
        for u, v in prerequisites:
            adjList[u].append(v)
        
        visit = set()

        def dfs(c):

            if not adjList[c]:
                return True
            
            if c in visit:
                return False
            
            visit.add(c)

            for nei in adjList[c]:
                if not dfs(nei):
                    return False
            
            visit.remove(c)
            adjList[c] = []
        
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True