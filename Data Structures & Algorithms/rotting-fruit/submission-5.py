class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        neighbours = [(0,1), (1,0), (-1,0), (0,-1)]

        time = 0
        
        while q:

            for _ in range(len(q)):

                r,c = q.popleft()

                for dr, dc in neighbours:

                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr,nc))
            
            if q:
                time += 1

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return time

