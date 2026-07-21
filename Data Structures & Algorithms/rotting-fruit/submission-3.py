class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        neighbours = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        
        time = 0

        while q:

            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in neighbours:
                    nr = dr + r
                    nc = dc + c

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited or grid[nr][nc] == 0 or grid[nr][nc] == 2:
                        continue

                    q.append((nr,nc))
                    visited.add((nr,nc))
                    grid[nr][nc] = 2
            
            if q:
                time += 1

        
        #print(visited)
        #print(grid)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1 
        
        return time

