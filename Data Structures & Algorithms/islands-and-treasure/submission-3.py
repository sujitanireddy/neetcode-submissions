class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        """  
        [2147483647,-1,0,1]
        [2147483647,2147483647,1,-1]
        [2147483647,-1,2147483647,-1]
        [0,-1,2147483647,2147483647]
        """
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        distance = 1
        neighbors = [(0,1),(1,0),(-1,0),(0,-1)]
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            for _ in range(len(q)):

                r, c = q.popleft()

                for dr, dc in neighbors:

                    nr = r + dr
                    nc = c + dc 

                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == -1 or grid[nr][nc] == 0 or (nr,nc) in visit:
                        continue
                    
                    grid[nr][nc] = distance
                    
                    q.append((nr,nc))
                    visit.add((nr,nc))
            
            distance += 1