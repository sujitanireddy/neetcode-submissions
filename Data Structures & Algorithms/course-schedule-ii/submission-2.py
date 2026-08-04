class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        """
        If there is a cycle in the graph then return empty array else return the order at which the courses can be finished.

        adjList
        visit = set()
        res = []



        """
        res = []
        visit = set()
        adjList = defaultdict(list)
        for c, p in prerequisites:
            adjList[c].append(p)
        
        def dfs(c):

            if c in res:
                return True
            
            if c in visit:
                return False
            
            visit.add(c)

            for nei in adjList[c]:
                if not dfs(nei):
                    return False
            
            res.append(c)
            visit.remove(c)

            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res
