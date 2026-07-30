class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        """
        Observations: If there is a cycle in the graph then we can say it's False
        0 -> 1
        adjlist = { 0 : [1] 
                    1 : [0]
                    }

        visit = {0,1}
        - Build the adjlist
        - For every course go check if it can be completed - Recursive DFS functions
            - Base case: If no prereq's then we can return True
            - We will use a visit hashset to track if this course has already been visited. (Cycle detection). If in hashset then: False
        - Backtrack and remove courses from visit set        
        """
        visit = set()


        #O(n)
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        #O(n * (V + E))
        #O(n)
        def dfs(c):

            if not adjList[c]:
                return True

            if c in visit:
                return False
            
            visit.add(c)

            for prereq in adjList[c]:
                if not dfs(prereq):
                    return False
            
            visit.remove(c)
            adjList[c] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True
