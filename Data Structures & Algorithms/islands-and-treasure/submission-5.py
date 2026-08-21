"""
[3,-1,  0, 1]
[2.  ,2, 1,-1]
[1 ,-1,  2,-1]
[0,  -1, 3,4]
"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
    
        neighbours = [(0,1),(1,0),(0,-1),(-1,0)]
        dist = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] == -1:
                        continue

                    grid[nr][nc] = dist
                    q.append((nr,nc))
                    visit.add((nr,nc))
            
            dist += 1