class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        """
        account for out of bounds, 0, 2
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        neigbors = [(1,0),(0,1),(-1,0),(0,-1)]
        q = deque()
        time = 0
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))

        while q:

            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in neigbors:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2 or (nr,nc) in visit:
                        continue
                    
                    grid[nr][nc] = 2
                    q.append((nr,nc))
                    visit.add((nr,nc))
            
            if q:
                time += 1
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1 

        return time

        
        
