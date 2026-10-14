"""
a -> b
0 <-> 1 
- cycle detection in a graph

Two ways:
- DFS for cycle detection
- Union-Find (Disjoin set) DataStructure way

{
    0   : [1]
    1   : []

}

go throug all courses and do DFS and if the course is in visit: return False immedielty. there is a cycle

DFS with cycle detection
TC: O(V+E)
SC: O(V+E)

Union Find DS
TC: O(V+E)
SC: O(V+E)



{
    0   : [1]
    1   : [0]

}

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {i:[] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visit = set()

        def dfs(course):
            
            if course in visit:
                return False
            
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































