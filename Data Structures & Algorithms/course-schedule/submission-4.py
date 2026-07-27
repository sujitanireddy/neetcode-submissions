class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        """
        Build a adjList using hashmap. {course: [prereq array]}
        DFS function: If not prereq then return True
                      If course in already visited then return False
                      While we are backtracking, we can also convert prereq array to null for the viisted ones as we will hit the base case early
        """

        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visit = set() #store the visited graph nodes

        def dfs(course):
            
            if not adjList[course]:
                return True
            
            if course in visit:
                return False
            
            visit.add(course)

            for c in adjList[course]:
                if not dfs(c):
                    return False
            
            visit.remove(course)
            adjList[course] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
