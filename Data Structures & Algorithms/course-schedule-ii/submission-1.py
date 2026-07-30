class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visit = set()
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        res = []

        def dfs(c):

            if c in visit:
                return False
            
            if c in res:
                return True
            
            visit.add(c)

            for prereq in adjList[c]:
                if not dfs(prereq):
                    return False
            
            res.append(c)
            visit.remove(c)

            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res