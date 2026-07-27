class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
        visit = set()
        q = deque()
        distance = 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:

            for _ in range(len(q)):

                r,c = q.popleft()

                for dr, dc in neighbors:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == -1 or (nr,nc) in visit or grid[nr][nc] == 0:
                        continue
                    
                    grid[nr][nc] = distance
                    visit.add((nr,nc))
                    q.append((nr,nc))
            
            distance += 1

        
                     





        
        