class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        for c, p in prerequisites:
            adjList[c].append(p)
        
        res = []
        processed = set()
        visit = set()
        
        def dfs(course):
            
            if course in visit:
                return False
            
            if course in processed:
                return True
            
            visit.add(course)

            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            
            visit.remove(course)
            processed.add(course)
            res.append(course)

            return True


        for c in range(numCourses):
            if c not in processed:
                if not dfs(c):
                    return []
        
        return res