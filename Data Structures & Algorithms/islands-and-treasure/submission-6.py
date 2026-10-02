"""

   0   1   2.  3
0  INF,-1,  0, INF
1  INF,INF,INF,-1
2  INF,-1, INF,-1
3  0,  -1, INF,INF

Algo:
BFS

DS:
Queue

Algoritm:
- Add all the treasure chests to the queue
- BFS
"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()
        neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
        dist = 1

        #adding all treasure chests to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        #matrix BFS
        while q:
            for i in range(len(q)):

                r, c = q.popleft()

                for dr, dc in neighbors:

                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] == -1:
                        continue
                    
                    grid[nr][nc] = dist
                    visit.add((nr,nc))
                    q.append((nr,nc))
            
            dist += 1
        

