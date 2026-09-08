class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {}

        for i in range(numCourses):
            adjList[i] = []

        for u, v in prerequisites:
            adjList[u].append(v)
        visit = set()

        def dfs(c):
            # base case
            if c in visit:
                return False

            visit.add(c)

            for nei in adjList[c]:
                if not dfs(nei):
                    return False

            adjList[c] = []
            visit.remove(c)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
