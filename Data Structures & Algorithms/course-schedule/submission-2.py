class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visit = set()

        def dfs(course):

            if course in visit:
                return False
            
            if not adjList[course]:
                return True

            visit.add(course)

            for c in adjList[course]:
                if not dfs(c):
                    return False
            
            visit.remove(course)
            adjList[course] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        
        