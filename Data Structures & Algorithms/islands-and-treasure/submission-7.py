class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbours = [(0,-1),(-1,0),(1,0),(0,1)]
        q = deque()
        dist = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:

            dist += 1

            for _ in range(len(q)):

                r, c = q.popleft()

                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 2147483647:
                        continue
                    
                    grid[nr][nc] = dist

                    q.append((nr,nc))