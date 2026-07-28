class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        length = 1
        visit = set()

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:

            for _ in range(len(q)):

                r, c = q.popleft()

                for dr, dc in neighbors:

                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visit or grid[nr][nc] == -1 or grid[nr][nc] == 0:
                        continue
                    
                    grid[nr][nc] = length
                    q.append((nr,nc))
                    visit.add((nr,nc))
            
            length += 1



