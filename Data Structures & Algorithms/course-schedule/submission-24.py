"""
4
0 -> 1 <-> 2
3
cycle detection in graph problem

v = {0,1,2,}

{
    0 : [1]
    1 : [2]
    2 : [1]
    3 : []
}

base case:
if adjList[c] == []:
    return True

if c in visit:
    return False

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        visit = set()
        
        def dfs(c):
            
            if adjList[c] == []:
                return True
            
            if c in visit:
                return False
            
            visit.add(c)

            for nei in adjList[c]:
                if not dfs(nei):
                    return False

            visit.remove(c)
            adjList[c] = []

            return True


        for c in range(numCourses):
            if c not in visit:
                if not dfs(c):
                    return False
        
        return True






