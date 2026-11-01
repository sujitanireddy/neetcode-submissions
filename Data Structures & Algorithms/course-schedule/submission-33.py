class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visit = set()

        
        def dfs(course):

            if course in visit:
                return False

            if adjList[course] == []:
                return True
            
            visit.add(course)

            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            
            visit.remove(course)
            adjList[course] = []

            return True


        for c in range(numCourses):
            if not dfs(c):
                return False

        return True 