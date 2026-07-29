class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visit = set()
        res = []

        def dfs(course):

            if course in visit:
                return False

            if course in res:
                return True

            visit.add(course)

            for c in adjList[course]:
                if not dfs(c):
                    return False

            res.append(course)
            visit.remove(course)

            return True            

        for c in range(numCourses):
             if not dfs(c):
                  return False
        
        return True