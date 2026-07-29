class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visit = set()


        def dfs(course):

            if not adjList[course]:
                return True
            
            if course in visit:
                return False
            
            visit.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False

            visit.remove(course)
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True