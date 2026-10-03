"""
3
0   1   2

1 -> 0
|    |   
2____|


dfs(1)

if cycle detected:
    return []

visit = set()

{
    1 : 4
    2 : 3
    0 : 2
}

dfs(0)
visit = {0,2,1}
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjList = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        res = []
        visit = set()
        processed = set()

        def dfs(c):
            
            if c in visit:
                return False

            if c in processed:
                return True

            visit.add(c)
            
            for nei in adjList[c]:
                if not dfs(nei):
                    return False
            
            visit.remove(c)
            processed.add(c)
            res.append(c)
            
            return True

        for c in range(numCourses):
            if c not in processed:
                if not dfs(c):
                    return []

        return res






